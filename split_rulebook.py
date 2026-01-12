
import pypdf
import os

pdf_path = "Final+Draft+Rulebook+2026+-+KT+Update.pdf"
output_dir = "Rulebook_Sections"

# Define sections with their (start_page, end_page) inclusive, 1-based
sections = {
    "00_Intro_General_Guidelines": (1, 9),
    "01_Knowledge_Tests": (10, 11),
    "02_Quran_Memorization": (12, 14),
    "03_Quran_Recitation": (15, 16),
    "04_2D_Art": (17, 21),
    "05_3D_Art": (22, 24),
    "06_Fashion_Design": (25, 29),
    "07_Digital_Art": (30, 32),
    "08_Photography": (33, 36),
    "09_Extemporaneous_Essay": (37, 40),
    "10_Extemporaneous_Speaking": (41, 43),
    "11_Original_Oratory": (44, 46),
    "12_Poetry": (47, 50),
    "13_Prepared_Essay": (51, 54),
    "14_Short_Fiction": (55, 58),
    "15_Spoken_Word": (59, 61),
    "16_Debate": (62, 68),
    "17_Math_Olympics": (69, 74),
    "18_MIST_Quiz_Bowl": (75, 78),
    "19_Improv": (79, 81),
    "20_Business_Venture": (82, 87),
    "21_Humanitarian_Service": (88, 91),
    "22_Nasheed_Rap": (92, 95),
    "23_Science_Fair": (96, 99),
    "24_Short_Film": (100, 104),
    "25_Social_Media": (105, 109),
    "26_Basketball": (110, 113),
}

try:
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Opened PDF with {total_pages} pages.")

    processed_pages = 0

    for name, (start, end) in sections.items():
        writer = pypdf.PdfWriter()
        
        # Adjust for 0-based indexing
        start_idx = start - 1
        end_idx = end # Slice is exclusive at end, so 'end' is correct index to stop BEFORE, wait... 
                      # if end is 9, we want index 8 included. Python slice [0:9] includes 0..8. 
                      # So valid range is start_idx : end_idx where end_idx = end.
        
        for i in range(start_idx, end): # Loop through inclusive range
            if i < total_pages:
                 writer.add_page(reader.pages[i])
            else:
                print(f"Warning: Page {i+1} out of range for section {name}")

        output_filename = os.path.join(output_dir, f"{name}.pdf")
        with open(output_filename, "wb") as f:
            writer.write(f)
        
        num_pages_section = end - start + 1
        processed_pages += num_pages_section
        print(f"Created {output_filename} ({num_pages_section} pages)")

    print(f"\nTotal pages processed: {processed_pages}")
    
    if processed_pages == total_pages:
        print("SUCCESS: All pages accounted for.")
    else:
        print(f"WARNING: Page count mismatch! Original: {total_pages}, Processed: {processed_pages}")

except Exception as e:
    print(f"Error: {e}")
