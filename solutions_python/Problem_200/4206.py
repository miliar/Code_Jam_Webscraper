import sys


def GetDataPerLine(f):
    # we will return array of digits to work with
    strLine = f.readline()
    strLine = strLine.strip(' \t\n\r')
    digitsArray = [0] * (len(strLine))
    
    for i in range (0, len(strLine)):
         digitsArray[i] = int(strLine[i])

    #print (digitsArray)
    return (digitsArray)    

def SolveQuestionPerTest(listOfInput):
    N = listOfInput
    digitsNumber = len(N)
    
    for i in range (0, digitsNumber-1):

        # check if we can leave this number or need to decrease by 1
        # if current digit is greater than its following digit than for sure we can stay with this digit and get best resuls
        if (N[i] < N[i + 1]):
            continue

        for j in range (i+1, digitsNumber):
            # if this condition is not true than current digit can stay
            if (N[i] > N[j]):
                # Update N to be ...(CurrentDigit - 1) 9..9 and return
                N[i] = N[i] - 1    
                for m in range (i+1, digitsNumber):
                    N[m] = 9
                return N
        
    return N    


def GetNumericValue(arrayDigits):

    stringForNumber = ""
    for i in range (0, len(arrayDigits)):
        stringForNumber = stringForNumber + str(arrayDigits[i])

    return int (stringForNumber)
                
    
Output = []
f = open('B-small-attempt1.in')
out = open ('B-small-attempt1.out', 'w')
T = int(f.readline())
print ('T = ' + str(T))
for i in range(0,T):
    strSolution = SolveQuestionPerTest ( GetDataPerLine(f) )
    numbericValue = GetNumericValue(strSolution)
    strCase = 'Case #' + str(i+1) + ': ' + str(numbericValue) + '\n'
    #print (strCase)
    out.write(strCase)

out.close()
