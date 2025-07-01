import re

def mask_name(text):
    text = str(text)
    words = text.split()
    masked_words = []
    for word in words:
        if len(word) > 0:
            masked_words.append(word[0] + "***")
        else:
            masked_words.append(word)
    return " ".join(masked_words)

def mask_email(text):
    text = str(text)
    return re.sub(r'([a-zA-Z0-9_.+-])[a-zA-Z0-9_.+-]*(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', r'\1***\2', text)

def mask_phone(text):
    text = str(text)
    digits_only = ''.join(filter(str.isdigit, text))
    match = re.search(r'(\d{3})(\d+)', digits_only)
    if match:
        return match.group(1) + '*' * len(match.group(2))
    return text

def mask_address(text):
    text = str(text)
    words = text.split()
    masked_words = []
    for word in words:
        if len(word) > 0:
            masked_words.append(word[0] + "***")
        else:
            masked_words.append(word)
    return " ".join(masked_words)

def mask_purchase_id(text):
    text = str(text)
    return re.sub(r'\b(\d{2})\d{4}\b', r'\1****', text)

def mask_text(text):
    masked_text = str(text)
    masked_text = mask_name(masked_text)
    masked_text = mask_email(masked_text)
    masked_text = mask_phone(masked_text)
    masked_text = mask_address(masked_text)
    masked_text = mask_purchase_id(masked_text)
    return masked_text