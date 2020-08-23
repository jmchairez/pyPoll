import os
import csv

votes = os.path.join("..", "Resources", "election_data.csv")



with open(votes) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    num_rows = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for rows in csvreader:
        num_rows += 1

        if (rows[2] == "Khan"):
            khan += 1
        elif (rows[2] == "Correy"):
            correy += 1
        elif (rows[2] == "Li"):
            li += 1
        else:
            otooley += 1

        

    all_votes = khan + correy + li + otooley
    khan_vote_per = round((khan / num_rows)*100,3)
    correy_vote_per = round((correy / num_rows)*100,3)
    li_vote_per = round((li / num_rows)*100,3)
    otooley_vote_per = round((otooley / num_rows)*100,3)

   