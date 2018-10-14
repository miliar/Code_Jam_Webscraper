with open("B-large.in") as f:
    s = f.read().splitlines()

def getLess(sVal):
    prevC = 0
    for i in range(len(sVal)):
        if int(sVal[i]) < prevC:
            newI = str(int(sVal[i])-1)
            nines = "9"*(len(sVal)-i)
            print(sVal[:(i-1)])
            if i == 1 and prevC == 1:
                return "9"*(len(sVal)-1)
            else:
                return getLess(sVal[:(i-1)]+str(prevC-1)+nines)
        else:
            prevC = int(sVal[i])
    return sVal

output = []
with open("output.txt","a") as f:
    for i in range(1,len(s)):
        f.write("Case #"+str(i)+": "+getLess(s[i])+"\n")





