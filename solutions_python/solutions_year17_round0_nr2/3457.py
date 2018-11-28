#!/usr/bin/env python3
import sys
import os.path
from pathlib import Path


def solve(N):
    digits = [int(d) for d in list(str(N))]
    result = []
    for i in range(len(digits) - 1):
        if digits[i] <= digits[i + 1]:
            result.append(digits[i])
        else:
            result.append(digits[i] - 1)
            result += [9] * (len(digits) - i - 1)
            for j in range(i, 0, -1):
                if result[j] < result[j - 1]:
                    result[j] = 9
                    result[j - 1] -= 1
            x = ''.join([str(d) for d in result])
            return str(int(x))
    return str(N)


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
            N = int(fdin.readline())

            result = solve(N)

            line = "Case #{:d}: {}\n".format(case_num, result)
            print(line, end='')
            fdout.write(line)
