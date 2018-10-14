t = int(raw_input())
for case in xrange(1, t+1):
    s = raw_input()
    n = int(s)
    s = list(s)
    stop = len(s)-1 # ?
    for i in range(len(s)-2, -1, -1):
        if s[i] > s[i+1]:
            stop = i
    if stop == len(s) - 1:
        res = n
    else:
        s[stop+1:] = ['9' for _ in xrange(len(s)-stop-1)]
        while stop is not None:
            s[stop] = str(int(s[stop]) - 1)
            if stop-1 >= 0 and s[stop-1] > s[stop]:
                s[stop] = '9'
                stop -= 1
            else:
                stop = None
        res = ''.join(c for c in s if c != '0')
    print("Case #{}: {}".format(case, res))