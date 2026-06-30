# -------------------------------------------------------------
# Version: 1.1 (Optimized Word Bag Logic - 70% Threshold)
# -------------------------------------------------------------

CHECK_LIMIT = 30
THRESHOLD = 0.70
STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'was', 'were', 'will', 'with'
}

def get_tokens(text):
    if not text:
        return set()
    # Fast filtering: Keeps only alphanumeric & splits by space
    return {
        w for w in ''.join(c for c in text.lower() if c.isalnum() or c.isspace()).split()
        if w not in STOP_WORDS
    }

current_tokens = get_tokens(record.name)

if current_tokens:
    # OPTIMIZATION: search_read is faster than looping over recordsets
    last_posts = env['blog.post'].search_read(
        [('id', '!=', record.id)],
        ['name'],
        order='id desc',
        limit=CHECK_LIMIT
    )
    
    for post in last_posts:
        existing_tokens = get_tokens(post['name'])
        
        if not existing_tokens:
            continue
            
        # Calculate Intersection
        match_count = len(current_tokens & existing_tokens)
        score = match_count / len(current_tokens)
        
        if score >= THRESHOLD:
            # Duplicate Found: Destroy Record
            record.unlink()
            break