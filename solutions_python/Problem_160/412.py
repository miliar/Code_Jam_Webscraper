#coding: utf-8
inf = 100000

def gcd (a, b):
    while b!=0:
        tmp = a % b
        a = b
        b = tmp
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

def list_lcm(list):
    rets1=ms
    while len(rets1)>1:
        rets=[]
        for i in xrange(len(rets1)/2):
            lcm1 =lcm(rets1[2*i], rets1[2*i+1])
            rets.append(lcm1)
        if len(rets1)%2 == 1:
            rets.append(rets1[-1])
        rets1 = rets[:]
    return rets1[0]

def cut_num(ms):
    lcm = list_lcm(ms)
    ret = 0
    for x in ms:
        ret += lcm/x
    return ret

def calc(n, b, ms):
    cut = cut_num(ms)
    if n%cut == 0:
        n=cut
    else:
        n=n%cut
    
    flags = [0 for i in xrange(b)]

    for i in xrange(n): 
        done = False
        min = inf
        argmin = inf
        for j in xrange(b):
            if flags[j] == 0:
                flags[j]+=ms[j]
                done = True
                min = 0
                argmin = j
                break
            if flags[j] < min:
                min = flags[j]
                argmin = j
        if done:
            #print i+1, ":", flags, argmin
            continue

        flags[argmin] += ms[argmin]

        for j in xrange(b):
            flags[j] = flags[j]-min
        #print i+1, ":", flags, argmin
    return argmin+1

t = int(raw_input())
for i in xrange(t):
    b, n = map(int, raw_input().split())
    ms = [int(x) for x in raw_input().split()]
    ans = calc(n, b, ms)

    print "Case #%d: %d" % (i+1, ans)
