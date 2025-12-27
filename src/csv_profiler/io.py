import csv
from pathlib import Path

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)