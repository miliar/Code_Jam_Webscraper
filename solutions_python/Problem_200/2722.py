def tidy(digitList):
    largestDigit = 0
    for i in range(len(digitList)):
        if digitList[i]>=largestDigit:
            largestDigit = digitList[i]
        else:
            return False
    return True

inFile = open('B-small-attempt0.in')
outFile = open('B-small-attempt0.out', 'w')
testCases = int(inFile.readline())
caseNo = 1
while caseNo <= testCases:
    case = inFile.readline().rstrip()
    number = [0]*len(case)
    for i in range(len(case)):
        number[i] = int(case[i])
    while not tidy(number):
        i = 0
        while number[i] < number [i+1]:
            i += 1
        while number[i]==0:
            i -= 1
        number[i]-=1
        for j in range(i+1,len(number)):
            number[j]= 9
    answer = 0
    for i in range (len(number)):
        answer = answer*10 + number[i]
    outFile.write('Case #%s: %s\n' % (caseNo,answer))
    print(answer)
    caseNo += 1
inFile.close()
outFile.close()