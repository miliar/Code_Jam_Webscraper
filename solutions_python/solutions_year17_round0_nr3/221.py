import numpy as np
from sortedcontainers import SortedDict

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            N, K = f.readline().split()
            sol = solve(int(N), int(K))
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return

def solve(N, K):
    sd = SortedDict()
    sd[N] = 1
    while K > 0:
        interval, count = sd.peekitem()
        if K <= count:
            a = (interval-1)//2
            b = interval-1-a
            return ' '.join(map(str, (max(a, b), min(a, b))))
        del sd[interval]
        a = (interval-1)//2
        b = interval-1-a
        for ab in [a, b]:
            if ab not in sd:
                sd[ab] = 0
            sd[ab] += count
        K -= count
            
            
            




dir = "./"

input_file = dir+"C-test.in"
output_file = dir+"C-test.txt"

input_file = dir+"C-small-1-attempt0.in"
output_file = dir+"C-small-1-attempt0.out"

input_file = dir+"C-small-2-attempt0.in"
output_file = dir+"C-small-2-attempt0.out"

input_file = dir+"C-large.in"
output_file = dir+"C-large.out"
'''
'''
parse(input_file, output_file)

