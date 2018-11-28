import utils

if __name__ == "__main__":
    inputFile = "inputQ1"
    #inputFile = "test"
    inputFile = "A-small-attempt2.in"

    inputFile = "A-large.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    for index in range(1, int(cases) + 1):
        print "case ", index
        rowData = inputData.next()
        rowData = rowData.strip()
        strs = rowData.split(' ')
        R = int(strs[0])
        C = int(strs[1])
        M = []
        for i in range(R):
            r = inputData.next()
            chars = list(r)
            M.append(chars)

        if index == 83:
            print M
        mark = [0]*C
        O = []
        for i in range(R):
            r = M[i]
            O.append(r)
            for j in range(C):
                if r[j] != '?':
                    if mark[j] != 0 and i > 0:
                        k = i -1
                        while k > -1 and O[k][j] == '?':
                            O[k][j] = r[j]
                            k -= 1
                        mark[j] = 0
                else:
                    mark[j] = 1
                    if i == R-1:
                        k = i - 1
                        while k > -1 and O[k][j] == '?':
                            k -= 1
                            continue
                        if k > -1:
                            for kk in range(k, i+1):
                                O[kk][j] = O[k][j]
                            mark[j] = 0

        if index == 83:
            print O
        l = C
        r = -1
        flag = True
        if index == 83:
            print mark
        for j in range(C):
            if index == 83:
                print l, r
            if mark[j] == 1:
                flag = False
                if l < j:
                    continue
                else:
                    l = j    
            else:
                if l < j:
                    for i in range(R):
                        for jj in range(l, j):
                            O[i][jj] = O[i][j]
                    l = C
                    flag = True
                r = j
        if index == 83:
            print O
        if not flag: 
            print r, O
            for i in range(R):
                for jj in range(r+1, C):
                    O[i][jj] = O[i][r]
            print O

        outputString = "Case #" + str(index)+ ":\n"
        #print outputString
        outputData.write(outputString)
        for i in range(R):
            r = O[i]
            line = ''.join(r)
            outputString = line 
            #print outputString
            outputData.write(outputString)
                
            
