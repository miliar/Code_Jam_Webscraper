#!/usr/bin/python

import sys

def min_from_hm(hm):
    h, m = hm.split(':')
    return int(h) * 60 + int(m)

def first(arr):
    if len(arr):
        return arr[0]
    else:
        return 99999;



def calc_requirements(in_a, in_b, out_a, out_b):

    req_a = 0
    req_b = 0

    cur_a = 0
    cur_b = 0

    while len(in_a) + len(in_b) + len(out_a) + len(out_b) != 0:

        min_time = min(first(in_a), first(in_b), first(out_a), first(out_b))
        if min_time in in_a:
            in_a = in_a[1:]
            cur_a += 1
        elif min_time in in_b:
            in_b = in_b[1:]
            cur_b +=1
        elif min_time in out_a:
            if cur_a == 0:
                req_a += 1
            else:
                cur_a -= 1
            out_a = out_a[1:]
        elif min_time in out_b:
            if cur_b == 0:
                req_b += 1
            else:
                cur_b -= 1
            out_b = out_b[1:]

    return req_a, req_b

if __name__ == '__main__':
    f = open(sys.argv[1])
    n_cases = int(f.readline())
    for case in range(n_cases):
        turnaround = int(f.readline())
        line = f.readline().split(' ')
        n_a, n_b = line
        n_a = int(n_a)
        n_b = int(n_b)

        sched_a = {}
        sched_b = {}

        in_a = []
        in_b = []
        out_a = []
        out_b = []

        for j in range(n_a):
            line = f.readline().split(' ')
            time_from, time_to = line
            sched_a[min_from_hm(time_from)] = min_from_hm(time_to)
            out_a.append(min_from_hm(time_from))
            in_b.append(min_from_hm(time_to) + turnaround)

        for j in range(n_b):
            time_from, time_to = [min_from_hm(hm) for hm in f.readline().split(' ')]

            sched_b[time_from] = time_to
            out_b.append(time_from)
            in_a.append(time_to+ turnaround)
        
        in_a.sort()
        in_b.sort()
        out_a.sort()
        out_b.sort()

        #print in_a, in_b
        #print out_a, out_b

        req_a, req_b = calc_requirements(in_a, in_b, out_a, out_b)
        
        print 'Case #%d: %d %d' % (case + 1, req_a, req_b)
