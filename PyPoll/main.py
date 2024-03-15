import csv
from pathlib import Path

def readfile(path):
    #Takes a file path and reads the lines, returning a list of lists
    with open(path) as file:
        csvreader = csv.reader(file, delimiter=",")
        lines = []
        for row in csvreader:
            lines.append(row)
        return lines

def writefile(path, total_votes, candidates, perc_votes, tot_cand_votes, winner):
    #Takes a file path and the calculated values and writes them to a .txt file
    with open(path + "\\results.txt", mode="w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("------------------------\n")
        txtfile.write(f'Total Votes: {total_votes}\n')
        txtfile.write("------------------------\n")
        for cand in candidates:
            txtfile.write(f'{cand}: {perc_votes[cand]}% ({tot_cand_votes[cand]})\n')
        txtfile.write("------------------------\n")
        txtfile.write(f'Winner: {winner}\n')
        txtfile.write("------------------------\n")

def cand_list(lines):
    #Takes the file lines and returns a list of all the candidates
    candidates = []
    for line in lines:
        if line[2] not in candidates:
            candidates.append(line[2])
    return candidates

def calc_votes_per_cand(lines):
    #Takes the file lines and calculates the total number of votes per candidate,
    #the percentage of votes per candidate returning two dictionaries
    total = len(lines)
    vote_count = {}
    perc_votes = {}
    for line in lines:
        if line[2] in vote_count:
            vote_count[line[2]] += 1
        else:
            vote_count[line[2]] = 1
    for cand, count in vote_count.items():
        perc_votes[cand] = round((count/total)*100, 3)
    return perc_votes, vote_count
    
def calc_winner(total_votes):
    #Takes the total_votes dictionary and iterates over it to determine who has the most votes, returning the winner as a string
    votes = 0
    for cand in total_votes:
        if total_votes[cand] > votes:
            votes = total_votes[cand]
            winner = cand
    return winner

def main():
    #Calculate all the data with the given csv file
    file_lines = readfile(Path("./Resources/election_data.csv"))
    header = file_lines.pop(0)
    total_votes = len(file_lines)
    candidates = cand_list(file_lines)
    perc_votes, tot_cand_votes = calc_votes_per_cand(file_lines)
    winner = calc_winner(tot_cand_votes)
    #Print the results
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
    for cand in candidates:
        print(f'{cand}: {perc_votes[cand]}% ({tot_cand_votes[cand]})')
    print("------------------------")
    print(f'Winner: {winner}')
    print("------------------------")
    #Write the results to a txt file
    writefile(Path("./analysis"), total_votes, candidates, perc_votes, tot_cand_votes, winner)

if __name__ == "__main__":
    main()