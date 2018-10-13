from __future__ import division
def read_mapped(func=lambda x:x):
    return map(func, raw_input().split(" "))
def read_array(N, func):
    l = []
    for i in range(N):
        l.append(func(raw_input()))
    return l
def read_int():
    return int(raw_input())
def read_str():
    return raw_input()
def read_float():
    return float(raw_input())

T = read_int()

for case in xrange(T):
    c, f, x = read_mapped(float)
    fcount = 0
    minans = 100000000
    prevsecs = 0
    rate = 2
    while True:
        secs = 0
        if fcount!=0:
            prevsecs = prevsecs+(c/rate)
            rate = rate+f

        secs = prevsecs+(x/rate)
        if not secs<minans: 
            break
        else: 
            minans = secs
        # print "fc:{}, secs: {}, rate:{}, prevsecs:{}"\
            # .format(fcount, secs, rate, prevsecs)
        fcount += 1
    print "Case #{}: {:.7f}".format(case+1, minans)
