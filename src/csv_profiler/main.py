from csv_profiler.io import read_csv_rows

def main() -> None:
    path = "data/sample.csv"
    rows = read_csv_rows(path)

    print(f"path={path}")
    print(f"rows={len(rows)}")

    if not rows:
        print("No rows were read. Check the file path and file content.")
        return

    print("first row:")
    print(rows[0])

if __name__ == "__main__":
    main()