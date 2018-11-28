#!/usr/bin/env python3
# Google Code Jam
# C. Recycled Numbers


def recycle(A, B):
    cycles = set()
    for n in range(A, B + 1):
        s = str(n)
        cycles.add(frozenset(s[m:] + s[:m] for m in range(len(s)) if s[m] != '0' and A <= int(s[m:] + s[:m]) <= B))
    npairs = 0
    for fset in cycles:
        # print(fset)
        n = len(fset)
        npairs += n * (n - 1) // 2
    return npairs

def main():
    with open('C.in') as fin, open('C.out', 'w') as fout:
        T = int(next(fin))
        for i, line in enumerate(fin):
            A, B = map(int, line.split())
            print('Case #%d:' % (i + 1), recycle(A, B), file=fout)


if __name__ == "__main__":
    main()
