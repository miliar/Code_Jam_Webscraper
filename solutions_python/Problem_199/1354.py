def flip(S):
    newS = '';
    for i in range(len(S)):
        if S[i] == '-':
            newS += '+'
        else:
            newS += '-'
    return newS

def minFlips(S,K):
    minFlips = 0
    for i in range(len(S)):
        if S[i] == '+':
            continue
        if  i > len(S) - K:
            return "IMPOSSIBLE"
        S = S[:i] + flip(S[i:K+i]) + S[i+K:]
        minFlips += 1
    return minFlips

        
def f(inFile,outFile):
    T = int(inFile.readline())
    for i in range(T):
        line = inFile.readline()
        split = line.split(' ')
    
        S = split[0]
        if split[1][-1] == '\n':
            split[1] = split[1][:-1]
        K = int(split[1])
        flips = minFlips(S,K)
        outFile.write("Case #" + str(i+1) + ": " + str(flips) + "\n")


inFile = open("C:/Users/USER/Downloads/A-large.in","r")
outFile = open("C:/Users/USER/Downloads/A-large-practice.out","w")
f(inFile,outFile)
inFile.close()
outFile.close()
