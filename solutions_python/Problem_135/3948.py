#! /usr/bin/env python

def main():
    
    ifh = open("input.txt.txt", "r")

    numOfCases = int(ifh.readline())
    #for all the cases
    count = 0
    for i in range(numOfCases):
        count += 1
        firstRowIndex = int(ifh.readline()) - 1 #indexes are base 0
        firstSetup = []
        #Given info 4 rows
        for i in range(4):
            line = ifh.readline()
            rowString = line.split(" ") #makes "1 2 3 4\n" => ["1", "2", "3", "4"]
            row = []
            for i in range(4):
                row.append(int(rowString[i]))
            firstSetup.append(row)

        secondRowIndex = int(ifh.readline()) - 1
        secondSetup = []
        #Given info 4 rows
        for i in range(4):
            line = ifh.readline()
            rowString = line.split(" ") #makes "1 2 3 4\n" => ["1", "2", "3", "4"]
            row = []
            for i in range(4):
                row.append(int(rowString[i]))
            secondSetup.append(row)

        rowOne = firstSetup[firstRowIndex]
        rowTwo = secondSetup[secondRowIndex]
        itemList = []
        for fItem in rowOne:
            for sItem in rowTwo:
                if fItem == sItem:
                    itemList.append(fItem)

        i = count
        if len(itemList) == 1:
            print("Case #{0}: {1}".format( i, itemList[0]))
        elif len(itemList) > 1:
            print("Case #{0}: Bad magician!".format(i))
        else:
            print("Case #{0}: Volunteer cheated!".format(i))

                  
if __name__ == '__main__':
    main()
        
