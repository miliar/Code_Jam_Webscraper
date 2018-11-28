import sys

T = int(raw_input())

empties = {}

def add_empties(e, n):
    if str(e) in empties:
        empties[str(e)] += n
    else:
        empties[str(e)] = n

for t in range(1, T+1):
    N,K = map(int, raw_input().split())

    if N == K:
        ma, mi = 0, 0
        print 'Case #%d: %d %d' % (t, ma, mi)
        continue

    empties = { str(N): 1 }

    while True:
        e = max(map(int, empties.keys()))
        num = empties[str(e)]
        del empties[str(e)]
        if num >= K:
            if e % 2 == 0:
                ma = e / 2
                mi = e / 2 - 1
            else:
                ma = mi = e / 2
            break
        else:
            K -= num
            if e % 2 == 0:
                add_empties(e / 2, num)
                add_empties(e / 2 - 1, num)
            else:
                add_empties(e / 2, 2 * num)
            #print empties

    print 'Case #%d: %d %d' % (t, ma, mi)
