#!/usr/bin/env python
import sys
if  __name__ == '__main__':
    filename = sys.argv[1]   
    inf = open(filename)
    sys.stdin = inf

    rs = ''
    T = int(raw_input())
    for case in range(1, T+1):
        A,B,K = (int(x) for x in raw_input().split())
        ans = 0
        for x in range(A):
            for y in range(B):
                if x & y < K:
                    ans += 1
        r = 'Case #%s: %s\n' % (case, ans)
        print r
        rs += r
    text_file = open(filename + '.out', "w")
    text_file.write(rs[:-1])
    text_file.close()
    print rs
