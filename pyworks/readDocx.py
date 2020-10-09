#! python3 
# readDocs.py - docsファイル名を渡すことでテキストを抜き出すget_text関数

import docx

def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)