
import pypdf

pdf_path = "Final+Draft+Rulebook+2026+-+KT+Update.pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}")
    
    for i, page in enumerate(reader.pages):
        if i > 60: break
        text = page.extract_text()
        lines = text.split('\n')
        # Print first few non-empty lines to identify headers
        header_lines = [line.strip() for line in lines if line.strip()][:3]
        print(f"Page {i+1}: {header_lines}")
        
except Exception as e:
    print(f"Error: {e}")
