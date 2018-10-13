#!/usr/bin/env python3
import sys
import os.path
from pathlib import Path


def solve(D, N, horses):
    duration = []
    for i in range(N):
        duration.append((D - horses[i][0])/horses[i][1])
    longest = max(duration)
    speed = D / longest

    return f"{speed:f}"


#
# Service functions
#
def get_infile(file=None):
    if file:
        return file, Path(file).stem
    me, ext = os.path.splitext(os.path.basename(sys.argv[0]))
    for postfix in ['-large-practice', '-large', '-small-practice', '-small-attempt', '-sample']:
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
            D, N = [int(d) for d in fdin.readline().split()]
            horses = []
            for i in range(N):
                k, s = [int(d) for d in fdin.readline().split()]
                horses.append([k, s])

            result = solve(D, N, horses)

            line = "Case #{:d}: {}\n".format(case_num, result)
            print(line, end='')
            fdout.write(line)
