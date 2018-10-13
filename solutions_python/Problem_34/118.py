import re
str = raw_input()
arr = str.split()
L, D, N = int(arr[0]), int(arr[1]), int(arr[2])

words = []
for i in xrange(D):
    words.append(raw_input())

def Split(str):
    res = []
    i = 0;
    while i < len(str):
        if str[i] != '(':
            res.append(str[i])
            i += 1
        else:
            j = str.find(')', i)
            res.append(str[i+1:j])
            i = j + 1
    return res

for k in xrange(N):
    w = Split(raw_input())
    res = 0;
    for i in xrange(D):
        fl = True
        for j in xrange(L):
            if not (words[i][j] in w[j]):
                fl = False
                break
        if fl: res += 1
    print "Case #%d: %d" % (k+1, res)