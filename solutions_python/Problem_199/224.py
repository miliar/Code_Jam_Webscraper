import math, collections
f = open('input.in','r')
g = open('output.txt','w')
"""
just consider how many '-' are there in all slots that have the same remainder mode k. Those numbers should have the same parity.
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    s, k = f.readline()[:-1].split(' ')
    k = int(k)
    s = [int(x == '+') for x in s]
    length = len(s) - k
    if k == 1:
        result = s.count(0)
    elif length < 0:
        result = 0 if all(s) else 'IMPOSSIBLE'
    else:
        result = 0
        for i in xrange(length+1):
            if s[i] == 0:
                for j in xrange(i, i+k):
                    s[j] = 1 - s[j]
                result += 1
        if not all(s[-k+1:]):
            result = 'IMPOSSIBLE'
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()