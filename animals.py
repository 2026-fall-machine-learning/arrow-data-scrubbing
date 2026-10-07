import csv
from collections import defaultdict

def race_time_to_seconds(race_time: str) -> int:
    minutes, seconds = race_time.split(":")
    return int(minutes) * 60 + int(seconds)

def seconds_to_race_time(total_seconds: float) -> str:
    total_seconds = round(total_seconds)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"

def main():
    totals = defaultdict(int)
    counts = defaultdict(int)

    with open("animals.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            meat_eater = row["meat_eater"]
            totals[meat_eater] += race_time_to_seconds(row["race_time"])
            counts[meat_eater] += 1

    for meat_eater in sorted(totals):
        avg_seconds = totals[meat_eater] / counts[meat_eater]
        print(f"{meat_eater}: {seconds_to_race_time(avg_seconds)}")

if __name__ == "__main__":
    main()
