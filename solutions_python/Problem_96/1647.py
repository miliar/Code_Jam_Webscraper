'''
Created on Apr 14, 2012

@author: Samuel
'''

f = None
try:
    f = open("B-large.in")
except IOError:
    pass
T = int(f.readline())

for i in range(T):
    split = f.readline().split()
    N = int(split[0])
    S = int(split[1])
    p = int(split[2])
    t = [int(val) for val in split[3:]]
    s = S
    res = 0
    for j in range(N):
        #g = int(math.ceil(t[j] / 3.))
        if t[j] % 3 == 0:
            if t[j] / 3 >= p:
                res += 1
            elif t[j] / 3 > 0 and t[j] / 3 + 1 >= p and s > 0:
                res += 1
                s -= 1
        elif t[j] % 3 == 1:
            if t[j] / 3 + 1 >= p:
                res += 1
        elif t[j] % 3 == 2:
            if t[j] / 3 + 1 >= p:
                res += 1
            elif t[j] / 3 + 2 >= p and s > 0:
                res += 1
                s -= 1
    print "Case #%d: %d" % (i + 1, res)       
