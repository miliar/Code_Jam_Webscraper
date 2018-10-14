infilecode = "BLI"

import sys

def isTidy(N):
    for i in range(len(N)-1):
        if N[i] > N[i+1]: return False
    return True


mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}

infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())
for case in range(1,T+1):
    ## Read inputs and calculate answer
    S = input()

    N = [int(s) for s in S]
    
    while(not isTidy(N)):
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                for j in range(i+1,len(N)):
                    N[j] = 9
                N[i]-=1
                break

    while(len(N) == 1 or N[0] == 0):
        if len(N) == 1: break
        N.pop(0)

    answer = "".join([str(s) for s in N])

    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)