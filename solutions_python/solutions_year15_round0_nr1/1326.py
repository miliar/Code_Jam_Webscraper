#coding=utf-8



T = int(raw_input())

for case in range(1, T + 1):
    _, S = raw_input().split()
    tot, invited = 0, 0
    for (i, ch) in enumerate(S):
        cnt = int(ch)
        if cnt != 0:
            if tot < i:
                invited += i - tot
                tot = i
            tot += cnt
    print "Case #%d: %d"%(case, invited)

