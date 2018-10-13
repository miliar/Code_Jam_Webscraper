import numpy as np

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            N = f.readline().split()[0]
            sol = solve(N)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return


def solve(N):
    li = list(map(int, N))
    prev_dig = -1
    pos_to_decrement = None
    for pos in range(len(li)):
        dig = li[pos]
        if dig > prev_dig:
            pos_to_decrement = pos
        elif dig == prev_dig:
            pass
        else:
            if li[pos_to_decrement] == 1:
                assert pos_to_decrement == 0
                return '9'*(len(li)-1)
            else:
                res = ''.join(map(str, li[0:pos_to_decrement]))
                res += str(int(li[pos_to_decrement])-1)
                res += '9'*(len(li)-pos_to_decrement-1)
                assert len(li) == len(res)
                return res
        prev_dig = dig
    return ''.join(map(str, li))





dir = "./"

input_file = dir+"B-test.in"
output_file = dir+"B-test.txt"

input_file = dir+"B-small-attempt0.in"
output_file = dir+"B-small-attempt0.out"

input_file = dir+"B-large.in"
output_file = dir+"B-large.out"
'''
'''
parse(input_file, output_file)

