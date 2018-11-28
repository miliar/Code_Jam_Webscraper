#!/usr/bin/python
import sys; #sys.setrecursionlimit(1000000)
import heapq as H

def schedule(dA, dB, T):
    # number of trains to start the day
    nA = [0]; nB = [0]

    # waiting queues, maintained sorted
    qA = []
    qB = []

    # sort on departure time
    dA.sort(key=lambda x:x[0])
    dB.sort(key=lambda x:x[0])
    while dA or dB:
        # find the queue for the the nearest departure
        # (depart q, station, and count, arrive q)
        if not dA:
            dq,ds,dc,aq = (qB,dB,nB,qA) 
        elif not dB:
            dq,ds,dc,aq = (qA,dA,nA,qB)
        else:
            dq,ds,dc,aq = (qA,dA,nA,qB) if dA[0][0] < dB[0][0] else (qB,dB,nB,qA)

        d,a = ds.pop(0)
        H.heappush(aq,a+T) # queue arrival

        if dq and dq[0] <= d:
            H.heappop(dq) # a train is ready, send it out
        else:
            dc[0] += 1 # no trains available, start another at the station
        
    return nA[0],nB[0]

def times_to_ints(s):
    d,a = s.split()
    dh,dm = map(int,d.split(":"))
    ah,am = map(int,a.split(":"))
    return (dh*60 + dm, ah*60 + am)

def main():
    global cache, eti, qs, S
    N = input()
    for n in range(1,N+1):
        T = input()
        NA,NB = map(int,raw_input().split())
        depart_A = []
        for a in range(NA):
            l = raw_input()
            depart_A.append(times_to_ints(l))

        depart_B = []
        for b in range(NB):
            l = raw_input()
            depart_B.append(times_to_ints(l))


        start_A, start_B = schedule(depart_A, depart_B, T)
        print "Case #%i: %i %i" % (n, start_A, start_B)

main()
