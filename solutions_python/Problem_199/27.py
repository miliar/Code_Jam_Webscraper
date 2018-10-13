import sys
T = int(raw_input())

def solve(cards, k):
    n = len(cards)
    res = 0

    flip_cnt = 0
    flip_mark = [0] * n

    for idx in xrange(n):
        if idx >= k:
            flip_cnt -= flip_mark[idx - k]

        cur_flip = 0 if cards[idx] == '+' else 1
        cur_flip += flip_cnt

        if cur_flip % 2 == 1:
            if idx + k > n:
                return "IMPOSSIBLE"
            flip_mark[idx] = 1
            flip_cnt += 1
            res += 1

    return res

cnt = 0
for line in sys.stdin:
    cnt += 1
    if cnt > T:
        break

    cards, k = line.split()
    k  = int(k)
    print "Case #%s: %s" % (cnt, solve(cards, k))
    
    
