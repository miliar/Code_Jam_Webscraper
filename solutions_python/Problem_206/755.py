import os
import sys
from decimal import Decimal


def process_file(in_name, out_name):
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            def read():
                while True:
                    l = fin.readline()
                    if len(l) == 0:
                        raise Exception('EOF')
                    l = l.strip('\n')
                    if len(l):
                        return l

            def write(*args):
                fout.write(' '.join(map(str, args)))

            t = int(fin.readline())
            for i in range(t):
                write(f'Case #{i + 1}: ')
                solve(read, write)


def solve(read, write):
    D, N = map(int, read().split())
    K, S = [], []
    for i in range(N):
        k, s = map(int, read().split())
        K.append(k)
        S.append(s)
    v = ans(D, K, S)
    write(f'{v}\n')


def ans(D, K, S):
    last_time = 0
    for k, s in zip(K, S):
        last_time = max(last_time, Decimal(D - k) / Decimal(s))
    ret = Decimal(D) / last_time
    return round(ret, 6)


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        in_name = args[1]
        out_name = args[2] if len(args) == 3 else (
            (in_name[:-3] if in_name.endswith('.in')
             else in_name) + '.out')
        process_file(in_name, out_name)
    else:
        for in_name in os.listdir():
            if in_name.endswith('.in'):
                out_name = in_name[:-3] + '.out'
                process_file(in_name, out_name)
