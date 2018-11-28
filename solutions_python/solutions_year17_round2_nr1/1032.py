import sys, copy;
from operator import itemgetter
"""class horse
    def __init__():
        #"""
def solve(d,n,k,s):
    ti = []
    for i in range(0, n):
        ti.append((0.0+d-k[i])/s[i])
    horses = []
    for i in range(0, n):
        horses.append([k[i],ti[i]])
    horses = sorted(horses, key=itemgetter(0))
    #print horses;

    filteredhorses = []
    for i in range(0, n):
        toIgnore = False
        for j in range(i+1, n):
            if horses[i][1] < horses[j][1]:
                toIgnore = True
                break;
                #ignore i
        if not toIgnore:
            filteredhorses.append(horses[i])
    #print filteredhorses
    maxT = filteredhorses[0][1]
    #print maxT
    for i in range(1, len(filteredhorses)):
        if filteredhorses[i][1] > maxT:
            maxT = filteredhorses[i][1]
    #print maxT;
    return (0.0 + d) / maxT;

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        d,n = map(int, f.readline().split())
        ki=[]
        si=[]
        for i in range(0, n):
            k,s = map(int, f.readline().split())
            ki.append(k)
            si.append(s)
        file.write(str(solve(d,n,ki,si)) + "\n")
file.close()            








