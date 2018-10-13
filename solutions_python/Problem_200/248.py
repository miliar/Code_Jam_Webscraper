infilecode = "BLI"

import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = os.path.join(dir_path, "".join(mapping[c] for c in infilecode))
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')
T = int(input())


def rest9(N, i):
    for j in range(i, len(N)):
        N[j] = "9"

def decrease(N, i):
    if i < 0:
        return
    
    if N[i] == "0":
        decrease(N, i-1)
        return
    
    N[i] = str(int(N[i]) - 1)
    rest9(N, i+1)



for case in range(1,T+1):
    N = list(input())


    print(N)

    if len(N) > 1:
        i = 1
        while i < len(N):
            if N[i-1] <= N[i]:
                i += 1
                continue
            else:
                decrease(N, i)
                i = max(i-1, 1)

    
    answer = "".join(N).lstrip("0")
    
    
    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
    print(" ")

output.close()
