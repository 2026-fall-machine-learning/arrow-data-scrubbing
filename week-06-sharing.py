"""Read data.csv using plain Python (no pandas), just the csv module."""

import csv

CSV_PATH = r"C:\Users\14145\OneDrive - Madison College\ML\uv-python-with-copilot-fun\data.csv"


ENDANGERMENT_LEVELS = ["Vulnerable", "Definitely endangered", "Severely endangered"]


def read_rows(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def split_endangerment_column(rows: list[dict[str, str]]) -> None:
    """Add a 1/0 column for each endangerment level based on 'Degree of endangerment'."""
    for row in rows:
        degree = row["Degree of endangerment"]
        for level in ENDANGERMENT_LEVELS:
            row[level] = "1" if degree == level else "0"


def print_table(rows: list[dict[str, str]], columns: list[str], max_width: int = 25) -> None:
    def cell(value: str) -> str:
        value = value.replace("\n", " ")
        return value if len(value) <= max_width else value[: max_width - 3] + "..."

    widths = {col: max(len(col), *(len(cell(row[col])) for row in rows)) for col in columns}

    header = " | ".join(col.ljust(widths[col]) for col in columns)
    print(header)
    print("-+-".join("-" * widths[col] for col in columns))
    for row in rows:
        print(" | ".join(cell(row[col]).ljust(widths[col]) for col in columns))


def main() -> None:
    rows = read_rows(CSV_PATH)
    split_endangerment_column(rows)
    print(f"Rows: {len(rows)}")
    print(f"Columns: {list(rows[0].keys())}")

    print("\nFirst 10 rows:")
    table_columns = [
        "Name in English",
        "Number of speakers",
        *ENDANGERMENT_LEVELS,
    ]
    print_table(rows[:10], table_columns)


if __name__ == "__main__":
    main()
