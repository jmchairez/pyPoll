import os
import csv

votes = os.path.join("..", "Resources", "election_data.csv")

with open(votes) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    num_rows = 0
    for rows in csvreader:
        num_rows += 1

    unique_candidate = []

    for row in csvreader:
        if row[2] not in unique_can:
            unique_candidate.append(row[2])

def print_data(poll_data):
    voter_id = int(poll_data[0])
    country = str(poll_data[1])
    candidate = str(poll_data[3])


print(f"Total Votes: {num_rows}")  