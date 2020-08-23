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

    candidates = {"Khan": khan, "Correy": correy, "Li": li, "O''Tooley": otooley}
    popular_winner = max(candidates, key=candidates.get)


#Print the final script
print("Election Results")
print("-------------------------")
print(f"Total Votes: {num_rows}")    
print("-------------------------")
print(f"Khan: {khan_vote_per}% ({khan})")
print(f"Correy: {correy_vote_per}% ({correy})")
print(f"Li: {li_vote_per}% ({li})")
print(f"O'Tooley: {otooley_vote_per}% ({otooley})")
print("-------------------------")
print(f"Winner {popular_winner}")
print("-------------------------")

file = open("results_pyPoll", "w")

file.write("Election Results")
file.write("\n-------------------------")
file.write(f"\nTotal Votes: {num_rows}")    
file.write("\n-------------------------")
file.write(f"\nKhan: {khan_vote_per}% ({khan})")
file.write(f"\nCorrey: {correy_vote_per}% ({correy})")
file.write(f"\nLi: {li_vote_per}% ({li})")
file.write(f"\nO'Tooley: {otooley_vote_per}% ({otooley})")
file.write("\n-------------------------")
file.write(f"\nWinner {popular_winner}")
file.write("\n-------------------------")

file.close()