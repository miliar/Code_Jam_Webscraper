# Google Code Jam 2017 1B A
'''
I'm going 300 distance
other horses at Speed Distance Time 
120             60    180      3
60              90    240      2.66 (8/3)
Solve recursive problem for horse starting at 60 who'll wait for other.
Going 180 (240-60) distance
60              60    120      2
No, second horse doesn't adjust speed to arrive at same time as
slowest.  He's inconsequential.  Slowest horse takes 3 hr, so we will
too.  300/3=100 kph.

Going 100 km
80              100   20       .2
70               10   30       3
answer: 100/3
So we need to find horse that arrives last.
Calculate Distance/speed = duration, find longest
'''
def doCase(s):
    distance = int(s[0])
    lastArrive = 0
    for i in range(int(s[1])):
        (location, speed) = map(float, raw_input().strip().split())
        dist = distance - location
        arrive = dist / speed
        lastArrive = max(lastArrive, arrive)
    return distance / lastArrive

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, doCase(raw_input().strip().split()))
