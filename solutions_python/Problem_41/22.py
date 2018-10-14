T = int(raw_input())

for t in xrange(T):
    str = raw_input()
    res = ''
    if len(str) == 1:
        res = str + '0'
    else:
        i = len(str) - 2
        while i >= 0 and str[i] >= str[i+1]:
            i -= 1
        if i >= 0:
            res = str[0:i]
            c = str[i]
            str = str[i:]
            d = [0]*10
            for i in xrange(len(str)):
                d[ord(str[i]) - ord('0')] += 1
            i = ord(c) - ord('0') + 1
            while d[i] == 0: i += 1
            res += chr(i + ord('0'))
            d[i] -= 1
            for j in xrange(10):
                res += chr(j + ord('0'))*d[j]
        else:
            d = [0]*10
            for i in xrange(len(str)):
                d[ord(str[i]) - ord('0')] += 1
            d[0] += 1
            i = 1
            while d[i] == 0: i += 1
            res = chr(i + ord('0'))
            d[i] -= 1
            for j in xrange(10):
                res += chr(j + ord('0'))*d[j]

    print "Case #%d: %s" % (t+1, res)