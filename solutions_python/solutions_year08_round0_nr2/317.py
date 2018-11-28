#!/usr/bin/python

A = 0
B = 1
ARRIVAL = 0
DEPARTURE = 1

def tominute(s):
    h, m = s.split(':')
    return 60*int(h) + int(m)

def solve():
    t = int(raw_input())
    na, nb = map(int, raw_input().split())
    trains = []
    for i in range(na+nb):
        dep, arr = map(tominute, raw_input().split())
        arr += t
        if i < na:
            trains.append( (dep, DEPARTURE, A) )
            trains.append( (arr, ARRIVAL, B))
        else:
            trains.append( (dep, DEPARTURE, B) )
            trains.append( (arr, ARRIVAL, A))

    num = [0, 0]
    count = [0, 0]

    trains.sort()
    for t, isdep, isb in trains:
        if not isdep:
            count[isb] += 1
        else:
            if not count[isb]:
                num[isb]+=1
            else:
                count[isb] -= 1
    print num[0], num[1]

if __name__ == '__main__':
    ncases = int(raw_input())
    for i in range(ncases):
        print 'Case #%d:' % (i+1),
        solve()

