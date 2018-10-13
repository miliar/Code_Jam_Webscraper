#!/bin/python
i = open('B-large.in')
o = open('code.out','w')



for t in range(int(i.readline())):
    g = [int(x) for x in i.readline().split(' ')]
    num_googlers = g[0]
    surprising = g[1]
    beat_score = g[2]
    scores = g[3:]
    total_beat = (beat_score * 3) - 2
    total_surprise = (beat_score * 3) - 4
    count = 0
    for score in scores:
        if score >= total_beat:
            count +=1
        elif score >= total_surprise and score >=1 and surprising:
            surprising -= 1
            count +=1
    o.write("Case #%d: %d"%(t+1, count)+"\n")

i.close()
o.close()