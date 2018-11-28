def tidyNumbers():
    file = open(input(),'r')
    outputfile = open('outputTidyNumbers.txt','w')
    first = True
    number = 0
    for i in file:
        if first == False:
            number += 1
            testcasei = i.strip('\n')
            for k in range(int(testcasei),-1,-1):
                haha = str(k)
                for l in range(len(haha) - 1):
                    if haha[l] > haha[l + 1]:
                        found = False
                        break
                    else:
                        found = True
                if found == True:
                    outputfile.write('Case #'+ str(number) + ': ' + str(haha) + '\n')
                    break
        if first == True:
            first = False


tidyNumbers()