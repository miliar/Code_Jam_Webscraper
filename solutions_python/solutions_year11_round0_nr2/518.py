
inFile = open("..\input.txt", "r")
outFile = open("..\output.txt", "w")

def solve(combine, oppose, invoke):
    result = []
    for c in invoke:
        flag = True
        print (result)
        print ("\n")
        if len(result) == 0:
            result.append(c)
            continue
        if (result[-1], c) in combine:
            result.append(combine[(result.pop(), c)])
            flag = False
        elif (c in oppose):
            for i in range(1, len(result) + 1):
                if result[-i] in oppose[c]:
                    result = []
                    flag = False
                    break
        
        if flag: result.append(c)
            
    return result;

def solve2(combine, oppose, invoke):
    result = []
    for c in invoke:
        flag = True
        print (result)
        print ("\n")
        if len(result) == 0:
            result.append(c)
            continue
        if (result[-1], c) in combine:
            result.append(combine[(result.pop(), c)])
            flag = False
        elif (c in oppose):
            for i in range(len(result)):
                if result[i] in oppose[c]:
                    result = result[:i]
                    flag = False
                    break
        
        if flag: result.append(c)
            
    return result;

N = int(inFile.readline())
cnt = 0
for line in inFile:
    cnt += 1
    combine = {}
    oppose = {}
    invoke = []
    
    llLine = line.split()
    for i in range(int(llLine.pop(0))):
        ll = list(llLine.pop(0))
        combine[(ll[0], ll[1])] = ll[2]
        combine[(ll[1], ll[0])] = ll[2]
    
    for i in range(int(llLine.pop(0))):
        ll = list(llLine.pop(0))
        
        if ll[0] in oppose:
            oppose[ll[0]].add(ll[1])
        else:
            oppose[ll[0]] = set()
            oppose[ll[0]].add(ll[1])
            
        if ll[1] in oppose :
            oppose[ll[1]].add(ll[0])
        else:
            oppose[ll[1]] = set()
            oppose[ll[1]].add(ll[0])
    
    llLine.pop(0)
    invoke = list(llLine.pop(0))
    
    result = solve(combine, oppose, list(invoke))
    
    resStr = "Case #" + str(cnt) + ": ["
    for c in result:
            resStr += (c + ", ")
    if len(result) > 0:resStr = resStr[:-2]
    resStr = resStr + "]" + "\n"
    print (resStr)
    outFile.write(resStr)
            
    

           
    
