from math import *

f = open("Bathroom Stalls.txt", "w")
T = int(input())
for i in range(T):
    N, K = [int(x) for x in input().split()]
    A = [N]
    output = [0, 0]
    for j in range(K):
        A.sort()
        M = A.pop()
        M = M-1
        output = [ceil(M/2), floor(M/2)]
        A.extend(output)
    f.write("Case #%d: %d %d\n"%(i+1, output[0], output[1]))
        
f.close()
