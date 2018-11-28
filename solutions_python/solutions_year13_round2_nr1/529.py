import os, math, sys
from pprint import pprint
import copy

def readints(fp):
    return map(int, fp.readline().split())


def list_without(lst, idx):
    return lst[:idx] + lst[idx+1:]

def solve():
    pass

def main():
    inpath = 'A-small-attempt0.in'
    outpath = os.path.splitext(inpath)[0] + '.out'

    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        T = int(infile.readline())
        for t in xrange(T):
            A, N = readints(infile)
            motes = readints(infile)

            motes.sort()

            i = 0
            for m in motes:
                if A <= m:
                    break
                A += m
                i += 1
            motes[:] = motes[i:]


            if A <= 1:
                ans = len(motes)
            else:
                ans = 0
                rem = len(motes)
                for m in motes:
                    adds = 0
                    while A <= m and adds < rem:
                        A += A - 1
                        adds += 1
                    if adds >= rem:
                        ans += rem
                        break
                    else:
                        ans += adds
                        A += m
                        rem -= 1

            outfile.write('Case #%d: %d\n' % (t+1,ans))







if __name__ == '__main__':
    main()
