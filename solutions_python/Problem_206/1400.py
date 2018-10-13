import math
def horse(arr,d):
    mini = math.inf
    for i in arr:
        dist = d - i[0]
        t = dist/i[1]
        s = d/t
        if s < mini:
            mini = s
    return mini

def f(inFile,outFile):
    T = int(inFile.readline())
    for i in range(T):
        D,N = inFile.readline().split()
        D,N = int(D),int(N)
        arr = []
        for j in range(N):
            K,S = inFile.readline().split()
            K,S = int(K), int(S)
            arr.append((K,S))
        num = horse(arr,D)
        outFile.write("Case #" + str(i+1) + ": " + str(num) +"\n")


inFile = open("C:/Users/USER/Downloads/A-Large.in","r")
outFile = open("C:/Users/USER/Downloads/A-Large.out","w")
f(inFile,outFile)
inFile.close()
outFile.close()
