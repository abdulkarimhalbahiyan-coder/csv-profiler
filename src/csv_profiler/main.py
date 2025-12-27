from csv_profiler.io import read_csv_rows

def main() -> None:
    path = "data/sample.csv"
    rows = read_csv_rows(path)

    print(f"path={path}")
    print(f"rows={len(rows)}")

    if rows:
        print("first row:")
        print(rows[0])

if __name__ == "__main__":
    main()