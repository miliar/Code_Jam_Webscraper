#!/usr/bin/env python
import sys
Chars = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']
Result = []

def parse_sign(ch):
    return (ch[0] == '-', Chars.index(ch[-1]))

def fill_result():
    global Chars
    Product = [
        ['1',  'i',  'j',  'k'],
        ['i', '-1',  'k', '-j'],
        ['j', '-k', '-1',  'i'],
        ['k',  'j', '-i', '-1']
    ]
    for ch1 in Chars:
        res = []
        for ch2 in Chars:
            neg1, c1 = parse_sign(ch1)
            neg2, c2 = parse_sign(ch2)
            product  = Product[c1][c2]
            neg3, c3 = parse_sign(product)
            neg = (neg1 ^ neg2) ^ neg3
            c3 = Chars[c3]
            if neg:
                res.append('-' + c3)
            else:
                res.append(c3)
        Result.append(res)
    chs = {}
    for i in range(len(Chars)):
        chs[Chars[i]] = i
    Chars = chs

fill_result()
T = input()
for t in range(T):
    L, X = map(int, raw_input().split())
    st = raw_input()[:L]
    last = [False] * len(Chars) * 4
    last[0] = True
    for i in range(L * X):
        now = []
        ch  = Chars[st[i % L]]
        # target char
        for j in range(len(Chars)):
            # stage
            for k in range(4):
                can = False
                for lastc in range(len(Chars)):
                    if not last[lastc * 4 + k]:
                        continue
                    result = Chars[Result[lastc][ch]]
                    if result == j:
                        can = True
                        break
                if not can and j == 0 and k:
                    for lastc in range(len(Chars)):
                        if not last[lastc * 4 + k - 1]:
                            continue
                        result = Chars[Result[lastc][ch]]
                        if result == k:
                            can = True
                            break
                now.append(can)
        last = now
    print 'Case #%d: %s' % (t + 1, 'YES' if last[3] else 'NO')
    sys.stdout.flush()
