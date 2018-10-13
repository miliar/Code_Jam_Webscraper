#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    
    line = sys.stdin.readline()[:-1].split()
    n = int(line.pop(0))

    li = [(line[i],int(line[i+1])) for i in range(0,n*2,2)]
    act_o = 1
    act_b = 1
    l = []
    for (p,t) in li:
        if p == 'O':
             l.append(('O',abs(t-act_o)))
             act_o = t
        if p == 'B':
             l.append(('B',abs(t-act_b)))
             act_b = t

    tot_time = 0
    time_last = 0
    while l:
        time = 0
        while (l and (l[0][0] == 'O')):
            time += max(l[0][1] - time_last,0) + 1
            time_last = 0
            l.pop(0)
        time_last = time
        tot_time += time_last
        if not l:
            break
        time = 0
        while (l and (l[0][0] == 'B')):
            time += max(l[0][1] - time_last,0) + 1
            time_last = 0
            l.pop(0)
        time_last = time
        tot_time += time_last

    print "Case #%d: %d" %(actual_case,tot_time)
