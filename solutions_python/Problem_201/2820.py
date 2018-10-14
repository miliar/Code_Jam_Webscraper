#!/usr/bin/env python
import sys


def calc(ifile):
    N, K = [int(v.strip()) for v in ifile.readline().split()]
    free_stacks = [N]
    for i in range(K):
        max_index = free_stacks.index(max(free_stacks))
        max_val = max(free_stacks)
        if i == K-1:
            return "{} {}".format((max_val) // 2, (max_val-1) // 2)
        else:
            del free_stacks[max_index]

            free_stacks.append(max_val//2)
            free_stacks.append((max_val-1)//2)


    # read ifile
    pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ifile = open(sys.argv[1])
    else:
        ifile = sys.stdin
    if len(sys.argv) > 2:
        ofile = open(sys.argv[2], 'w')
    else:
        ofile = sys.stdout
    for i in range(int(ifile.readline())):
        ofile.write("Case #%i: %s\n" % (i+1, calc(ifile)))
