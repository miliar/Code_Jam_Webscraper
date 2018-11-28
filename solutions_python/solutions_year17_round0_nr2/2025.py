numCases = int(raw_input())
for case in range(1, numCases+1):
    N = int(raw_input())
    answer = N
    isN = 0
    strN = str(N)
    increasing = 1
    j = len(strN)-1
    while j>0:
        if (int(strN[j])>=int(strN[j-1])):
            j = j-1
        else:
            increasing = 0
            break
    if increasing:
        isN = 1
    if not isN:
        done = 0
        while not done:
            i = 0
            while i<len(strN)-1:
                if (int(strN[i])>int(strN[i+1])):
                    if not strN[i]=='1':
                        replace = int(strN[i])-1
                        numNines = len(strN)-1-i
                        strN = strN[:i]+str(replace)
                        for num in range(numNines):
                            strN = strN + '9'
                        break
                    else:
                        numNines = len(strN)-1
                        strN = ""
                        for num in range(numNines):
                            strN = strN + '9'
                        break
                else:
                    i=i+1
            increasing = 1
            j = len(strN)-1
            while j>0:
                if (int(strN[j])>=int(strN[j-1])):
                    j = j-1
                else:
                    increasing = 0
                    break
            if increasing:
                done = 1
    print "case #"+str(case)+": "+strN
