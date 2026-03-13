import pypdf

def extract_text(pdf_path):
    print(f"--- Extracting {pdf_path} ---")
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        for page in reader.pages:
            print(page.extract_text())
    print("-" * 40)

extract_text('KPC卒演.pdf')
extract_text('冬定期演奏会(仮2).pdf')
