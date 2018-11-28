#!/usr/bin/python

# simulate using dict

def doit():
    data = raw_input().strip().split()
    c = int(data[0])
    form = dict()
    for x in xrange(c):
        s = data[x + 1]
        form[s[0]] = (s[1], s[2])
        form[s[1]] = (s[0], s[2])
    d = int(data[c + 1])
    oppose = dict()
    for x in xrange(d):
        s = data[x + c + 2]
        oppose[s[0]] = s[1]
        oppose[s[1]] = s[0]
    n = int(data[c + d + 2])
    seq = data[c + d + 3]
    result = []
    count = dict() # may be more than 1
    for x in xrange(n):
        a = seq[x]
        if len(result) and a in form and form[a][0] == result[-1]: # form
            # remove the last 
            b = result[-1]
            count[b] -= 1
            if count[b] == 0:
                del count[b]
            result.pop()
            # add the newly formed
            b = form[a][1]
            if b not in count:
                count[b] = 0
            count[b] += 1
            result.append(b)
        elif a in oppose and oppose[a] in count: # clear
            result = []
            count = dict()
        else: # just add it
            result.append(a)
            if a not in count:
                count[a] = 0
            count[a] += 1
    print repr(result).replace("'", "")


n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1),
    doit()
