import numpy as np

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            D, N = map(int, f.readline().split())
            rows = []
            for _ in range(N):
                rows.append(list(map(int, f.readline().split())))
            sol = solve(D, N, rows)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return


def solve(D, N, rows):
    last_to_arrive = None
    for k, s in rows:
        if last_to_arrive is None:
            last_to_arrive = (k, s)
        else:
            k1, s1 = last_to_arrive
            if (D-k)*s1 > (D-k1)*s:
                last_to_arrive = (k, s)
    k1, s1 = last_to_arrive
    return D*s1/(D-k1)



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


