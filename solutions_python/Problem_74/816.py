#!/usr/bin/python

cases = input()
for case in xrange(1,cases+1):
    line = raw_input()
    line = line.split()
    n = int(line[0])
    pos = {'O':1, 'B':1}
    time = {'O':0, 'B':0}
    total_time = 0
    for i in xrange(1,n+1):
        player = line[2*i-1]
        position = int(line[2*i])
        t = abs(position - pos[player]) 
        time[player] += t
        pos[player] = position
        if time[player] <= total_time:
            time[player] = total_time   # 4 O 2 B 1 B 2 O 4
        else:
            total_time = time[player]
        time[player] += 1
        total_time += 1
    print "Case #%d: %d"%(case,total_time)
