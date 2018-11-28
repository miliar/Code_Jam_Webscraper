T = input()
for t in range(T):
    l = [int(x) for x in raw_input().split()]
    N = l.pop(0)
    S = l.pop(0)
    P = l.pop(0)
    l.sort(reverse=True)

    res = 0
    for score in l:
        rem = score % 3
        if rem == 0:
            val = score / 3
            if val >= P:
                res += 1
            elif score > 0 and S > 0 and val + 1 >= P:
                S -= 1
                res += 1
        elif rem == 1:
            val = score / 3 + 1
            if val >= P:
                res += 1
        else:
            val = score / 3 + 1
            if val >= P:
                res += 1
            elif S > 0 and val + 1 >= P:
                S -= 1
                res += 1
        

    print 'Case #%d: %d' % (t+1, res)
