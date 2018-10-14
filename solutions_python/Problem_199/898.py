import utils


def checkOnes(l):
    ones = 0
    last = -1
    for i in range(len(l)):
        if i > 0:
            last = l[i - 1]
        if l[i] == 0:
            if last == 1:
                ones += 1
            else:
                continue
        else:
            if last == 1:
                continue
            else:
                continue
    return ones

if __name__ == "__main__":
    inputFile = "inputQ1"
    inputFile = "A-small-attempt3.in"
    #inputFile = "B-small-attempt0.in"
    #inputFile = "test"
    #inputFile = "B-large.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        #print "case ", index
        rowData = inputData.next()
        rowData = rowData.strip()
        strs = rowData.split(' ')
        k = int(strs[1])
        L = len(strs[0]) 
        F = ['+'] * L
        strF = ''.join(F)


        flag = True
        old = strs[0]
        List = []
        if old == strF:
            flag = False
        List.append(old)
        step = 0
        visited = {}
        visited[old] = 1
        while(flag):
            flag1 = True
            newList = []
            for oldE in List:
                for i in range(L - k + 1):
                    new = oldE
                    newS = list(new)
                    for j in range(i, i + k):
                        if newS[j] == '+':
                            newS[j] = '-'
                        else:
                            newS[j] = '+'
                    new = ''.join(newS)
                    if index == 10:
                        print new
                    if new == strF:
                        flag1 = False
                        flag = False
                        break
                    else:
                        if new not in visited:
                            newList.append(new)
                            visited[new] = 1
                            flag1 = False
            if flag1:
                flag = False
                step = -1
            else:
                step += 1
                del List[:]
                List = newList[:]
        
        o = str(step)
        if step == -1:
            o = 'IMPOSSIBLE'
        outputString = "Case #" + str(index)+ ": " + o + "\n"
        #print outputString
        outputData.write(outputString)
                
            
