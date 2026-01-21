from pathlib import Path
from datetime import datetime
import pandas as pd

def combine_excels(input_dir: Path, output_dir: Path):
    excel_files = list(input_dir.glob("*.xlsx"))

    if not excel_files:
        print("No Excel files to combine.")
        return None

    dfs = []
    for file in excel_files:
        df = pd.read_excel(file)
        df["source_file"] = file.name
        dfs.append(df)

    final_df = pd.concat(dfs, ignore_index=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"combined_{timestamp}.xlsx"
    final_df.to_excel(output_file, index=False)
    return output_file
