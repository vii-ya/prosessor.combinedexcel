from pathlib import Path
from combine_excel import combine_excels

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    excel_files = list(INPUT_DIR.glob("*.xlsx"))
    print(f"DEBUG: Found {len(excel_files)} Excel files in {INPUT_DIR.resolve()}")

    if not excel_files:
        print("No Excel files found. Exiting.")
        return

    file_created = combine_excels(INPUT_DIR, OUTPUT_DIR)
    if file_created:
        print(f"DEBUG: File created at {file_created.resolve()}")

if __name__ == "__main__":
    main()
