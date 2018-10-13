# filenames
filein = "B-large.in.txt"
fileout = "B.large.answers"

# functions
def cleanRight(strNumber, start):
    strNumber = strNumber[:start] + (len(strNumber) - start)*'9'
    return strNumber

def cleanLeft(strNumber, i):
    if (strNumber[i] == '1'):
        if (i == 0):
            strNumber = strNumber[1:]
        else:
            strNumber = strNumber[:i] + '9' + strNumber[i+1:]
            strNumber = cleanLeft(strNumber, i-1)
    else:
        newDigit = str(int(strNumber[i]) - 1)
        strNumber = strNumber[:i] + newDigit + strNumber[i+1:]
        if ((strNumber[i-1] > strNumber[i]) == True):
            strNumber = largest_tidy(strNumber)
    return strNumber

def largest_tidy(strNumber):
    if (len(strNumber) == 1):
        return strNumber
    for i in range(len(strNumber)-1):
        if ((strNumber[i] > strNumber[i+1]) == True):
            strNumber = cleanRight(strNumber, i+1)
            strNumber = cleanLeft(strNumber, i)
            return strNumber
    return strNumber

# reading and writing files
answers = open(fileout, 'w')
with open(filein) as file:
    numlist = file.readlines()
    nitems = int(numlist[0])
    for i in range(1,nitems+1):
        num = numlist[i].strip('\n')
        num = largest_tidy(num)
        answers.write("case #" + str(i) + ": " + num + '\n')
