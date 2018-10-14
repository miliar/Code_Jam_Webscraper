def numberOfZeros(line):
    counter = 0
    for digit in line:
        if (digit == "0"):
            counter += 1
    return counter

def alreadyInOrder(pancakeRow):
    if (pancakeRow == '+' * len(pancakeRow)):
        return True
    else:
        return False
    

def turn(pancakes, index):
    if (pancakes[index] == '+'):
        pancakes[index] = '-'
        return "".join(pancakes)
    elif (pancakes[index] == '-'):
        pancakes[index] = '+'
        return "".join(pancakes)

def findMinIndex(pancakeRow):
    for i in range(len(pancakeRow)):
        if (pancakeRow[i] == '-'):
            return i

def fewPancakesToTurn(pancakeRow, flipSize, startIndex):
    if (len(pancakeRow) - flipSize - startIndex < 0):
        return True
    else:
        return False
        
    

def flip(pancakeRow, flipSize, startIndex=0, flipCount=0):
    print("In flip ", pancakeRow)

    if (alreadyInOrder(pancakeRow)):
        return (True, flipCount)
    elif (fewPancakesToTurn(pancakeRow, flipSize, startIndex)):
        return (False, 42)

    # Going to flip again, increase flip count
    flipCount += 1
    
    for i in range(flipSize):
        pancakes = list(pancakeRow)
        print("in turn pancakes", pancakes)
        pancakeRow = turn(pancakes, startIndex+i)

    return flip(pancakeRow, flipSize, findMinIndex(pancakeRow), flipCount)

    

## Open the file with read only permit
f = open('input.txt', "r")
fp = open('output.txt',"w")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

for i in range(len(lines)):    
    if (i == 0):
        continue

    # process input line
    pancakeRow,flipSize = lines[i].split(" ")

    # check if row already in order
    if (alreadyInOrder(pancakeRow)):
        fp.write("Case #" + str(i) + ": 0" + "\n")
        continue


    # flip
    success, numberOfFlips = flip(pancakeRow, int(flipSize),findMinIndex(pancakeRow))


    # Print results
    if (success):
        fp.write("Case #" + str(i) + ": " + str(numberOfFlips) + "\n")
    else:
        fp.write("Case #" + str(i) + ": " + "IMPOSSIBLE" + "\n")
    
    
    

    
        

## close the file after reading the lines.
f.close()
fp.close()




    
