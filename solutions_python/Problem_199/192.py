import sys


def main():
    inputFile = open(sys.argv[1], "r")
    numCases = int(inputFile.readline())
    for n in range(1,numCases+1):
        s, k = inputFile.readline().split(" ")
        k = int(k)
        pancakes = []
        for i in range(len(s)):
            pancakes.append(s[i])
        numFlips = 0
        for i in range(0,len(pancakes)-k+1):
            if pancakes[i] == "-":
                for j in range(i,i+k):
                    if pancakes[j] == "-":
                        pancakes[j] = "+"
                    else:
                        pancakes[j] = "-"
                numFlips += 1
        allUp = True
        for i in range(len(pancakes)-k+1,len(pancakes)):
            if pancakes[i] == "-":
                allUp = False
        if allUp:
            print("Case #%i: %i"%(n,numFlips))
        else:
            print("Case #%i: %s"%(n,"IMPOSSIBLE"))
    
main()