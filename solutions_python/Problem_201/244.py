infilecode = "XI"

import sys
import os 
import math
dir_path = os.path.dirname(os.path.realpath(__file__))
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
infile = "C-large.in"
infile = os.path.join(dir_path, infile)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')
T = int(input())

solutions = {}


def solve(N, K):
    if N == K:
        return (0, 0)
    if N <= 0 or K <= 0 or N < K:
        raise Exception("Error")

    if K == 1:
        return (N//2, (N-1)//2)

    if (N, K) in solutions:
        return solutions[(N, K)]
    
    AN = (N-1)//2
    BN = N - AN - 1
    kLeft = (K-1)//2
    kRight = (K - 1) - kLeft

    options = []
    if kLeft > 0:
        A = solve(AN, kLeft)
        options.append(A)

    if kRight > 0:
        B = solve(BN, kRight)
        options.append(B)

    
    #options.append(min([A, B], key=lambda x: (x[1], x[0])))
    #options.extend([A, B])
    best = min(options, key=lambda x: (x[1], x[0]))
    solutions[(N, K)] = best
    return best

for case in range(1,T+1):
    N, K = input().split()
    N = int(N)
    K = int(K)
    print(N, K)



    best = solve(N, K)

    
    answer = str(best[0]) + " " + str(best[1])
    
    
    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
    print(" ")

output.close()
