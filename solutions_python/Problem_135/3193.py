PATH = r"C:\Users\Gil\Documents\jam\input.txt"

def solveGame(data):
    firstRowNum = int(data[0][0])
    firstRow = data[firstRowNum]
    secondRowNum = int(data[5][0])
    secondRow = data[5+secondRowNum]

##    print firstRowNum, secondRowNum
    
    numbers = []

##    print "first row", firstRow
##    print "second row", secondRow
##
    for num in firstRow:
        if num in secondRow:
##            print num
            numbers.append(num)

    
##    raw_input(" a ")
    
    if len(numbers) == 0:
        return "Volunteer cheated!"
    elif len(numbers) > 1:
        return "Bad magician!"
    else:
        return str(numbers[0])
    

data = open(PATH,"r").readlines()
data = [x.replace("\n","") for x in data]
data = [[int(i) for i in x.split(" ") ] for x in data]

numOfGames = int(data[0][0])

output = ""

for i in range(numOfGames):
    output += "Case #%s: " % (i+1)
    output += solveGame(data[1+i*10:1+(i+1)*10])
    output += "\n"

output = output.rstrip("\n")

print output



    
