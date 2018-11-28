#!/usr/bin/python

t = raw_input()

def get_next(s):
    res = {}
    flag = True
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i+1]:
            flag = False
            break
    if flag == True:
        s = '0' + s
        i = 0
    for k in range(len(s)):
        res[k] = s[k]

    for j in range(len(s) - 1, -1, -1):
        if s[i] < s[j]:
            break
    res[i] = s[j]
    res[j] = s[i]

    #print str(res)
    r = len(s) - 1;
    f = i + 1;

    while (r > f): 
        tmp = res[f]
        res[f] = res[r]
        res[r] = tmp
        r -= 1
        f += 1
        #print res
    m = ''
    for i in range(len(s)):
        m += res[i]
    return m


for i in range(0, int(t)):
    stri = raw_input()
    result = get_next(stri)
    #print result
    #    print res
    print 'Case #'+str(i+1)+': '+result
