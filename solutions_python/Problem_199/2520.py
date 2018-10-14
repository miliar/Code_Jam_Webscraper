t = int(raw_input())                                   # test cases
for i in xrange(1, t+1):
    l = map(str, raw_input())
    temp = l.index(' ')
    k = int(''.join(l[temp+1:]))
    del l[temp:]
    len_l = len(l)
    d = {}
    ans, count = 0, 0
    while(count < len_l):
        if(l[count]=='+'):
            count += 1
            continue
        if(count+k <= len_l):
            for j in xrange(count, count+k):
                if(l[j]=='-'):
                    l[j] = '+'
                else:
                    l[j] = '-'
                try:
                    d[l[j]].append(j)
                except:
                    d[l[j]] = []
                    d[l[j]].append(j)
            if('-' in d):
                count = d['-'][0]
            else:
                count += k
        else:
            count += k    
        d.clear()
        ans += 1
    if('-' in l):
        ans = 'IMPOSSIBLE'
    print "Case #{}: {}".format(i, ans)