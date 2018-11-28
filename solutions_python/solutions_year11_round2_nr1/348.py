#!/usr/bin/env python
import pprint as pp

owp = {}

def read():
    N = int(raw_input())
    data = [0]*N
    for i in xrange(N):
        data[i] = []
        for el in raw_input():
            if el=='.': data[i].append(None)
            else: data[i].append(int(el))
    return N, data

def RR(res, cnt): return float(res)/cnt

def WP(data, t, N, x = -1):
    res, cnt = 0, 0
    for i in xrange(N):
        if i == x: continue
        d = data[t][i]
        if d==1: res+=1
        if not d is None: cnt += 1
    return RR(res, cnt)

def OWP(data, t, N):
    global owp
    if not t in owp: 
        res, cnt = 0, 0
        for i in xrange(N): 
            if not data[t][i] is None:
                cnt += 1
                res += WP(data, i, N, t)
        owp[t] = RR(res, cnt)
    return owp[t]

def OOWP(data, t, N):
    res, cnt = 0, 0
    for i in xrange(N): 
        if not data[t][i] is None:
            cnt += 1
            res += OWP(data, i, N)
    return RR(res, cnt)

def stat(data,t,N):
    RPI = 0.25 * WP(data,t,N) + 0.50 * OWP(data,t,N) + 0.25 * OOWP(data,t,N)
    return str(RPI)

def run_test():
    N, data = read()
    global owp
    owp = {}
    s = [stat(data,i,N) for i in xrange(N)]
    return "\n".join(s)

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i: \n%s"%(test+1, str(run_test()))

main();
