
# --- CONFIGURATION (Change categories and keywords here) ---
CATEGORY_A_KEYWORDS = ['keyword1', 'keyword2', 'keyword3']
CATEGORY_B_KEYWORDS = ['keyword4', 'keyword5', 'keyword6']

# Extract and tokenize title
title_pieces = record.name.lower().split() if record.name else []

# --- ROUTING LOGIC ---
if any(piece in CATEGORY_A_KEYWORDS for piece in title_pieces):
    record.write({'blog_id': x})  # Category A

elif any(piece in CATEGORY_B_KEYWORDS for piece in title_pieces):
    record.write({'blog_id': x})  # Category B

else:
    record.write({'blog_id': x})  # Default Fallback Category