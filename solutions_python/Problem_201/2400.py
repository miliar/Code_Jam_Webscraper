#!/usr/bin/env python3
import sys
import os.path
from pathlib import Path


def solve(N, K):
    occupied = [0, N + 1]

    for i in range(K):
        pos, ls, rs = find(N, occupied)

    return "{:d} {:d}".format(max(ls, rs), min(ls, rs))


def find(N, occupied):
    longest = 0
    p = 0
    for i in range(len(occupied) - 1):
        dist = occupied[i + 1] - occupied[i]
        if dist > longest:
            longest = dist
            p = i
    # print(p, longest)
    half = longest // 2
    pos = occupied[p] + half
    # print("occupy:", pos)
    occupied.insert(p + 1, pos)
    ls = occupied[p + 1] - occupied[p] - 1
    rs = occupied[p + 2] - occupied[p + 1] - 1
    # print(occupied)
    return pos, max(ls, rs), min(ls, rs)


#
# Service functions
#
def get_infile(file=None):
    if file:
        return file, Path(file).stem
    me, ext = os.path.splitext(os.path.basename(sys.argv[0]))
    for postfix in ['-large-practice', '-large', '-small-practice', '-small-1-attempt', '-sample']:
        files = sorted(Path('.').glob(me + postfix + '*'), reverse=True)
        for file in files:
            if file.suffix == '.txt':
                infile = Path(file.stem)
            else:
                infile = file
            if infile.suffix == '.in':
                return file.name, infile.stem
    raise FileNotFoundError('No input files')


#
# main
#
input_file, stem = get_infile()
print('Input:  {}\nOutput: {}.out\n'.format(input_file, stem))

with open(input_file, "r") as fdin:
    with open(stem + ".out", "w") as fdout:
        T = int(fdin.readline())
        for case_num in range(1, T + 1):
            N, K = [int(d) for d in fdin.readline().split()]

            result = solve(N, K)

            line = "Case #{:d}: {}\n".format(case_num, result)
            print(line, end='')
            fdout.write(line)
