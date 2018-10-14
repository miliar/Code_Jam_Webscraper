# mylist = []
# mylist.append(5)
# x
#
# def functionName():
#     #code
#     global x
#
#
# with open('in.txt', 'r') as inFile: #'w' for write
#     l = inFile.readline()
#     splited = l.split()
#     for c in l:
#         #code
#     for i in range(5):
#         #code
#     # write code
#
#


def replaceKMinusAndPlus ( line, K,indexOfMinus):
    Kstr = line[indexOfMinus:(indexOfMinus+K)]
    strIndx = 0
    for str in Kstr:
        if (str=='+'):
            Kstr = Kstr[:strIndx] + '-' + Kstr[strIndx+1:]
            strIndx +=1
        elif (str=='-'):
            Kstr = Kstr[:strIndx] + '+' + Kstr[strIndx+1:]
            strIndx +=1
        else:
            print("error in Kstr")
    return Kstr

def checkLine(line):
    for str in line:
        if (str == '-'):
            return False
    return True



with open('in.txt','r') as inFile, open('out.txt', 'w') as outFile :
    caseNum = 0
    for line in inFile:
        if (caseNum == 0):    # handle the first line
           T = int(line)
           caseNum += 1
        else: # handle cases
            splitted = line.split()
            S = list(splitted[0])
            K = int(splitted[1])
            indexOfMinus = 0
            numOfFlips=0

            for i in range (len(S)): #use the greedy algo
                if ((S[i]=='-') and ((i + int(K) - 1)< len(S)) ): #todo check
                    indexOfMinus = i
                    numOfFlips +=1
                    for j in range(i,(i+K)):
                        if (S[j] == '+'):
                            S[j] = '-'
                        else:
                            S[j] = '+'
                    # S = S[:indexOfMinus] + replaceKMinusAndPlus(S,K,indexOfMinus)+S[(indexOfMinus+K):]

            if (checkLine(S)):#check if the line is possible
                outFile.write('Case #' + str(caseNum) +': ' + str(numOfFlips) +'\n')
            else:
                outFile.write('Case #' + str(caseNum) +': ' + "IMPOSSIBLE"+'\n')

            caseNum += 1


