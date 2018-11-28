import sys
import re

input = sys.stdin
T=int(input.readline())




def process(data):
    res = []
    wp = {}
    owp = {}
    oowp = {}

    for i in xrange(len(data)):
        w = len(re.sub('[^1]','',data[i]))
        a = len(re.sub('[^01]','',data[i]))
        wp[i] = float(w)/a


    for i in xrange(len(data)):
        c = 0
        n = 0
        ss = data[i]
        for j in xrange(len(data)):
            if i == j:
                continue
            if ss[j] not in ('0', '1'):
                continue
            s = data[j]
            s = s[:i]+'_'+s[i+1:]
            n += 1
            w = len(re.sub('[^1]','',s))
            a = len(re.sub('[^01]','',s))
            c += float(w)/a
            # print i, j, s, float(w)/a
        owp[i] = c/n

    for i in xrange(len(data)):
        s = data[i]
        c = 0
        n = 0
        for j in xrange(len(s)):
            if s[j] in ('0', '1'):
                c += owp[j]
                n += 1
        oowp[i] = float(c)/n

    # print wp
    # print owp
    # print oowp
    for i in xrange(len(data)):
        res.append(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])
    return res


for i in xrange(1,T+1):
    N=int(input.readline())
    data = []
    for j in xrange(N):
        s = input.readline().strip()
        data.append(s)
    res = process(data)
    print "Case #%s:" % i
    for r in res:
        print r

