t = int(raw_input())
for case in xrange(1, t+1):
    s, sz = raw_input().split()
    s = list(s)
    sz = int(sz)
    flips = 0
    res = 0
    for i, c in enumerate(s):
        if c == '-':
            end = i + sz
            if end > len(s):
                res = "IMPOSSIBLE"
                break
            res += 1
            for j in xrange(i, i+sz):
                s[j] = ['+', '-'][s[j] == '+']
    print("Case #{}: {}".format(case, res))    