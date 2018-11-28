tcs = int(raw_input())
for t in range(1,tcs+1):
    num = raw_input()
    len_n = len(num)
    it = len_n - 1
    mins = 9
    pivot = -1
    while it>=0:
        d = int(num[it])
        if d > mins:
            pivot = it
            mins = d - 1
            key = mins
        else:
            mins = d
        it-=1
    if pivot!=-1:
        answer = num[:pivot] + str(key) + '9'*(len_n - pivot - 1)
    else:
        answer = num
    print 'Case #{}: {}'.format(t, int(answer))

