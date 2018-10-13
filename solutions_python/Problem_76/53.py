#!/usr/bin/python
N = int(raw_input())
for x in xrange(1,N+1):
    raw_input()
    numbers = sorted(map(int,raw_input().split(" ")))
    print "Case #"+str(x)+": "+(reduce(lambda a,b:a^b, numbers) and "NO" or str(reduce(lambda a,b:a+b, numbers[1:])))
