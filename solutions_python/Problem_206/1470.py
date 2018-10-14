# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:55:51 2017

@author: elon
"""

cases = int(raw_input())
for i in xrange(1, cases+1):
    dist, horsesNum = raw_input().split(" ")
    dist = int(dist)
    horsesNum = int(horsesNum)
    horses = []
    for j in xrange(horsesNum):
        postion, speed = raw_input().split(" ")
        horses.append([int(postion), int(speed)])
    anw = float(10000000000000)
    for j in horses:
        postion = float(j[0])
        speed = float(j[1])
        distLeft = dist - postion
        hoursToGet = distLeft/speed
        if dist/hoursToGet < anw:
            anw = dist/hoursToGet
    realAnw = str("%.6f" % anw)
    print "Case #"+str(i)+": "+realAnw