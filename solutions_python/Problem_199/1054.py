with open("A-large.in") as f:
    s = f.read().splitlines()

def flipBit(cakeStr,i):
    if cakeStr[i] == "+":
        return cakeStr[:i]+"-"+cakeStr[(i+1):]
    else:
        return cakeStr[:i]+"+"+cakeStr[(i+1):]

def flip(cakeStr,i,k):
    for j in range(i,i+k):
        cakeStr = flipBit(cakeStr,j)
    return cakeStr
        

with open("output.txt","a") as f:
    testCount = 1
    for line in s[1:]:
        cakes, k = line.split(" ") 
        k = int(k)
        counter = 0
        for i in range(0,len(cakes)-k+1):
            if cakes[i] == "-":
                cakes = flip(cakes,i,k)
                counter += 1
        if cakes != len(cakes)*"+":
            f.write("Case #"+str(testCount)+": IMPOSSIBLE\n")
        else:
            f.write("Case #"+str(testCount)+": "+str(counter)+"\n")
        testCount += 1
