import csv
import os

def readfile(filepath):
    #Takes a file path and reads the lines, returning a list of lists
    with open(filepath) as file:
        csvreader = csv.reader(file, delimiter=",")
        lines = []
        for row in csvreader:
            lines.append(row)
        return lines
    
def writefile(filepath, total_months, net_amount, avg_change, greatest_profit, greatest_loss):
    #Takes a file path and the calculated values and writes them to a .txt file
    with open(os.path.join(filepath, "results.txt"), mode="w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f'Total Months: {total_months}\n')
        txtfile.write(f'Total: {net_amount}\n')
        txtfile.write(f'Average Change: {avg_change}\n')
        txtfile.write(f'Greatest Increase in Profits: {greatest_profit[0]} (${greatest_profit[1]})\n')
        txtfile.write(f'Greatest Decrease in Profits: {greatest_loss[0]} (${greatest_loss[1]})\n')
    
def calc_months(lines):
    #Takes in the file lines and calculates the total months in the dataset, returning a number
    total_months = len(lines)
    return total_months
    

def calc_net_amount(lines):
    #Takes in the file lines and calculates the net amount of profit/loss, returning a number
    net_total = 0
    for line in lines:
        net_total += int(line[1])
    return net_total
        
def calc_profit_loss_change(lines):
    #Takes in the file lines and calculates the average change month to month,
    #the greatest monthly profit and the greatest monthly loss, returning a number and two lists
    greatest_profit = ["", 0]
    greatest_loss = ["", 0]
    previous_profit = 0
    profit_loss_change = []
    total_months = 0
    #Loop through the lines and subtract the current month from the previous month to find change in profit/loss
    for line in lines:
        total_months += 1
        if total_months > 1:
            change = int(line[1]) - previous_profit
            profit_loss_change.append(change)
            if change > greatest_profit[1]:
                greatest_profit[0] = line[0]
                greatest_profit[1] = change
            elif change < greatest_loss[1]:
                greatest_loss[0] = line[0]
                greatest_loss[1] = change
        previous_profit = int(line[1])
    #Calculate the average from the list of changes and the number of monthly changes
    average = round(sum(profit_loss_change) / (len(lines) - 1), 2)
    return average, greatest_profit, greatest_loss

def main():

    file_lines = readfile(os.path.join("C:\\Users\\mckin\\Documents\\python-challenge\\PyBank\\Resources\\budget_data.csv"))
    print(file_lines)
    header = file_lines.pop(0)
    total_months = calc_months(file_lines)
    net_amount = calc_net_amount(file_lines)
    avg_change, greatest_profit, greatest_loss = calc_profit_loss_change(file_lines)
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: {net_amount}')
    print(f'Average Change: {avg_change}')
    print(f'Greatest Increase in Profits: {greatest_profit[0]} (${greatest_profit[1]})')
    print(f'Greatest Decrease in Profits: {greatest_loss[0]} (${greatest_loss[1]})')
    writefile(os.path.join("C:\\Users\\mckin\\Documents\\python-challenge\\PyBank\\analysis"), total_months, net_amount, avg_change, greatest_profit, greatest_loss)

if __name__ == "__main__":
    main()