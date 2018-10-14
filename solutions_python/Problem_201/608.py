import sys
import itertools

def parse(line):
    return map(int,line.split())

def solve(case):
    N,K = case
    rep = 1 << K.bit_length() # ceil power of 2
    i = N - K
    Ls = i // rep
    Lr = (i + rep // 2) // rep
    return f'{max(Ls, Lr)} {min(Ls, Lr)}'

input_file = sys.argv[1]
with open(input_file) as f:
    lines = [line.strip() for line in f]
cases = map(parse,lines[1:])
ys = map(solve,cases)
output_file = input_file.replace('input','output')
with open(output_file,'w') as f:
    for i,y in enumerate(ys):
        f.write(f'Case #{i+1}: {y}\n')
