infilecode = "ALI"

import sys
#import networkx as nx
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())

for case in range(1,T+1):
    
    D, N = list(map(int, input().split()))
    horse = [ list(map(int, input().split())) for i in range(N) ]

    best = -1
    for K, S in horse:
        dist = D - K
        time = dist / S
        if best == -1:
            best = time
        else:
            best = max(best,time)
    print(best)

    answer = D / best

    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)