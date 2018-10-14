#coding: utf-8
import sys
INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'
sys.stdin = file(INPUT_FILE, 'r')
sys.stdout = file(OUTPUT_FILE, 'w')


T = int(raw_input())
for case in xrange(1, T+1):
    S, K = raw_input().split(' ')
    S, K = list(S), int(K)
    ret, ans = '', 0
    while True:
        pos = -1
        for i in range(len(S)):
            if S[i] == '-' and i + K <= len(S):
                pos = i
                break
        if pos != -1:
            ans += 1
            for i in range(K):
                S[i+pos] = '+' if S[i+pos] == '-' else '-'
        ok = True
        for cake in S:
            if cake == '-':
                ok = False
                break

        if ok: break
        elif pos == -1 and not ok:
            ans = 'IMPOSSIBLE'
            break
    print 'Case #%d: %s' % (case, str(ans))
