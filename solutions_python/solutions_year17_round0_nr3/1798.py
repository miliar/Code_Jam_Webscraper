#!/usr/bin/env python
print("Enter file name: ")
inFileName = input()
print("Enter output name: ")
outFileName = input() + ".txt"

inFile = open(inFileName, 'r')

data = inFile.readlines()

data = [line.strip("\n") for line in data]

def solveProblem(n, k):
    stalls = [n]
    for i in range(k):
        maxi = 0
        for j in range(len(stalls)):
            if stalls[j] > stalls[maxi]:
                maxi = j
        
        if(stalls[maxi]%2): #if odd
            stalls[maxi] = int((stalls[maxi] - 1)/2)
            stalls.insert(maxi+1, stalls[maxi])
        else:# if even
            stalls[maxi] = int((stalls[maxi] - 1)/2)
            stalls.insert(maxi+1, stalls[maxi] + 1)
        #print(stalls)
    last = stalls[maxi], stalls[maxi+1]
    return max(last), min(last)

nInputs = data[0]
data.pop(0)

results = []

#print(data)

for line in data:
    n,k = line.split(" ")
    results += [solveProblem(int(n),int(k))]


outFile = open(outFileName,"w") 

for i in range(int(nInputs)):
    line = "Case #{}: {} {}\n".format(i + 1, results[i][0], results[i][1])
    outFile.write(line)
    print(line.strip("\n"))
 
outFile.close()


