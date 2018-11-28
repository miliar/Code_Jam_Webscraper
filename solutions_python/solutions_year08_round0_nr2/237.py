#!/usr/bin/env python
import sys
import datetime

TIME_FMT = "%H:%M"

def readfrom(l, n, id, t, fd):
    for i in xrange(n):
        s, e = fd.readline().split()
        st = datetime.datetime.strptime(s, TIME_FMT)
        et = datetime.datetime.strptime(e, TIME_FMT)
        et += datetime.timedelta(minutes=t)
        l.append((st, et, id))

def getminstart(l):
    f = datetime.datetime.strptime("23:59", TIME_FMT)
    fe = datetime.datetime.strptime("23:59", TIME_FMT)
    idx = -1
    for n, t in enumerate(l):
        s, e, id = t
        if s < f:
            f = s
            fe = e
            idx = n
        elif s == f:
            if e < fe:
                f = s
                fe = e
                idx = n
    return idx

def getavail(l, t, id):
    for n, (s, i) in enumerate(l):
        if i != id:
            continue
        if s <= t:
            return n
    return -1

def main():
    #file_in = open("B-sample.in")
    file_in = sys.stdin
    file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        taround = int(file_in.readline())
        n_froma, n_fromb = map(int, file_in.readline().split())
        fromList = []
        readfrom(fromList, n_froma, 0, taround, file_in)
        readfrom(fromList, n_fromb, 1, taround, file_in)

        n_trains = [0, 0]
        trainavail = []
        while len(fromList):
            n = getminstart(fromList)
            s = fromList.pop(n)
            a = getavail(trainavail, s[0], s[2])
            if a == -1:
                n_trains[s[2]] += 1
            else:
                trainavail.pop(a)
            trainavail.append((s[1], (s[2]+1) % 2))

        print "Case #%d: %d %d" % (i+1, n_trains[0], n_trains[1])

    #file_out.close()
    #file_in.close()

if __name__ == '__main__':
    main()