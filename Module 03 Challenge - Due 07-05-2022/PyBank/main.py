
import os
import csv

budget_csv = os.path.join( "Resources", "budget_data.csv")
outputFile = os.path.join("Resources", "budget_data_output.txt")

Total_Months = 0
Total_Net = 0

netChangesNumbers = []
dateList = []
greatestIncrease = []
greatestDecrease = []

with open(budget_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)
    csv_header = next(csvfile)
    
    firstRow = next(csv_reader)
    Total_Months += 1
    Total_Net += int(firstRow[1])
    firstValue = float(firstRow[1])
    

    for row in csv_reader:
        
        Total_Months += 1
        Total_Net += int(row[1])
        netChange = float(row[1]) - float(firstValue)
        netChangesNumbers.append(netChange)
        dateList.append(row[0])
        firstValue = float(row[1])
        
    
        
    AverageChange = (sum(netChangesNumbers)) / (len(netChangesNumbers))
    
    greatestIncrease = [dateList[0], netChangesNumbers[0]]
    greatestDecrease = [dateList[0], netChangesNumbers[0]]
    

    for i in range (0, len(netChangesNumbers)):

        if(netChangesNumbers[i] > greatestIncrease[1]):
            greatestIncrease[1] = int(netChangesNumbers[i])
            greatestIncrease[0] = dateList[i]
        
        if(netChangesNumbers[i] < greatestDecrease[1]):
            greatestDecrease[1] = int(netChangesNumbers[i])
            greatestDecrease[0] = dateList[i]
    
    
    output = (
        f"Financial Analysis \n"
        f"--------------------- \n"
        f"Total Months: {Total_Months}\n"
        f"Total: ${Total_Net}\n"
        f"Average Change: ${AverageChange:.2f}\n"
        f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
        f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})"
    )

    print(output)

with open(outputFile, "w") as textfile:
    textfile.write(output)
        