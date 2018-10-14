#!/usr/bin/python

from math import *

f=open('problem_1_large.in', 'r')
output=open('problem_1_large.out', 'w')

cases=int(f.readline())

def finish_time(d, pos, speed):
    return (float(d) - pos) / float(speed)

for case in range(cases):
    arr=f.readline().replace("\n","").split(' ')
    d=int(arr[0])
    n=int(arr[1])
    horses=[]
    for i in range(n):
        arr=f.readline().replace("\n","").split(' ')
        pos=int(arr[0])
        speed=int(arr[1])
        if pos < d: horses.append((pos,speed))
    min_finsh_time=max([ finish_time(d, pos, speed) for (pos, speed) in horses])
    value=(float(d) / min_finsh_time)
    # print "Case #%i: %s" % (case+1, value)
    # output.write ("Case #%i: %s\n" % (case+1, value))
    output.write ("Case #%i: %s\n" % (case+1, str(value)))
