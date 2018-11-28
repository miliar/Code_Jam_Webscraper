import numpy as np

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            S, K = f.readline().split()
            sol = solve(S, int(K))
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return

def flip(s, k):
    assert s in '+-'
    if k%2:
        if s == '-':
            return '+'
        else:
            return '-'
    else:
        return s

def solve(S, K):
    N = len(S)
    positions = N-K+1
    flips = np.zeros((N,))
    moves = 0
    for i in range(positions):
        curr_side = flip(S[i], flips[i])
        if curr_side == '-':
            moves += 1
            flips[i:i+K] += 1
    for i in range(positions, N):
        curr_side = flip(S[i], flips[i])
        if curr_side == '-':
            return 'IMPOSSIBLE'
    return moves



dir = "./"

input_file = dir+"A-test.in"
output_file = dir+"A-test.txt"

input_file = dir+"A-small-attempt0.in"
output_file = dir+"A-small-attempt0.out"

input_file = dir+"A-large.in"
output_file = dir+"A-large.out"
'''
'''
parse(input_file, output_file)

