from pypdf import PdfReader
import os

def extract_text_from_pdf(file_path):
    
    try:
        reader = PdfReader(file_path)
        text_chunk=[] 
        for i,page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text_chunk.append(page_text)
                else:
                    pass
        full_text = " ".join(text_chunk)

        if not full_text.strip():
            return "",f"Document does not contain any text"
        
        return full_text, None
    
    except Exception as e:
        return "",f"File has error {e}"




