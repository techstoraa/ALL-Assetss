if record.content:
    try:
        clean_content = record.content
        if hasattr(clean_content, 'decode'):
            clean_content = clean_content.decode('utf-8')
            
        while '<' in clean_content and '>' in clean_content:
            start = clean_content.find('<')
            end = clean_content.find('>', start)
            if end == -1:
                break
            clean_content = clean_content[:start] + clean_content[end+1:]
            
        clean_content = clean_content.strip()
    except Exception:
        clean_content = str(record.content).strip()
    
    if len(clean_content) < 200:
        raise UserError("Content must be greater than 200 characters.")
else:
    raise UserError("Content cannot be empty.")
      