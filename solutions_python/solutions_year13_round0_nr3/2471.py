# source code for GCJ2013 qualification round
# by Pengyu CHEN(cpy.prefers.you@gmail.com)
# COPYLEFT, ALL WRONGS RESERVED.

import sys
import itertools
import bisect

def gen():
    for i in range(50):
        print("progress: %d/50" %(i + 1), file=sys.stderr)
        for j in range(min(5, i + 1 + 1)):
            for k in itertools.combinations(range(i + 1), j):
                l = ['0'] * (i + 1)
                for x in k:
                    l[x] = '1'
                yield ''.join(l)
    pass

def main():
    l = [0, 1, 2, 3, 22]
    for i in gen():
        def check_and_add(l, s):
            i = int(s)
            s1 = str(i ** 2)
            if s1 == s1[::-1]:
                l += [i]
            pass
        check_and_add(l, i + i[::-1])
        check_and_add(l, i + '0' + i[::-1])
        check_and_add(l, i + '1' + i[::-1])
        check_and_add(l, i + '2' + i[::-1])
        check_and_add(l, '2' + i + i[::-1] + '2')
        pass
    l.sort()
    l = l[100:]
    l = list(map(lambda x: x ** 2, l))
    print("ready", file=sys.stderr)
    
    T = int(input())
    for t in range(T):
        a, b = list(map(lambda x: int(x), input().split()))
        n = bisect.bisect_right(l, b) - bisect.bisect_left(l, a)
        print("Case #%d: %d" %(t + 1, n))
    pass

if __name__ == "__main__":
    main()
