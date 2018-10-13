#!/usr/bin/env python

import sys

def permute(num):
    a = []
    strnum = str(num)
    for i in range(len(strnum)):
        a.append(int(strnum[i:] + strnum[0:i]))
    return a

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    num_cases = int(f.readline().strip())
    count = 0
    for line in f:
        count += 1
        start = int(line.split()[0])
        end = int(line.split()[1])
        cur = start
        total = 0
        perms = []
        while cur < end:
            for perm in permute(cur):
                if cur < perm and perm <= end and (cur,perm) not in perms:
                    perms.append((cur,perm))
                    total += 1
                elif (cur,perm) in perms:
                    print(cur,perm)
            cur += 1
        print 'Case #%d: %s' % (count, total)
    f.close()

