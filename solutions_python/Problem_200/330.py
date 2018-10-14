
T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    digits = []
    while N > 0:
        digits.append(N % 10)
        N /= 10
    digits = list(reversed(digits))

    cur_smallest = 0
    sto_smallest = []
    for n in xrange(len(digits)):
        sto_smallest.append(cur_smallest)
        cur_smallest = max([cur_smallest, digits[n]])

    
    stick = []
    for n in xrange(len(digits)):
        if sto_smallest[n] > digits[n]: # cannot stick here liao
            stick.append(False)
        else:
            stick.append(True)
    
    ans = []
    for n in xrange(len(digits)):
        if stick[n]:
            continue

        # set all to 9's here and forever
        ans = [9] * (len(digits)-n)
        break
    
    if len(ans) > 0:
        OK = False
    else:
        OK = True
        n = len(digits)

    for n in xrange(n-1, -1, -1):
        if OK == True:
            ans.append(digits[n])
            continue

        if sto_smallest[n] == digits[n]:
            ans.append(9)
        else:
            ans.append(digits[n]-1)
            OK = True

    total = 0
    ans = list(reversed(ans))
    for x in xrange(len(ans)):
        total = total * 10 + ans[x]

    print 'Case #%d: %d' % (t+1, total)


    

