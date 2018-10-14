#!/usr/local/bin/python
# coding: utf-8

import re
import os
import sys
import urllib2
import urllib
import cookielib
import codecs
import math
from time import time

reload(sys)
sys.setdefaultencoding("utf-8")
streamWriter = codecs.lookup('utf-8')[-1]
sys.stdout = streamWriter(sys.stdout)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

def sumQ(L, queue):
    ret = list()
    for i in L:
        ret.append(sum(map(lambda(x):queue[int(x)], i.split("-")[:-1][0:len(queue)])))
    return ret

def TPReps(size, queue):
    groups = list()
    rep =  list()
    offset = list()
    ride = (0,"")
    tam = len(queue)
    i = 0
    while i < 100000000:
        n = queue[i%tam]
        if ride[0]+n <= size:
            ride = (ride[0] + n, ride[1] + (str(i%tam)+"-"))
        else:
            if ride[1] in groups:
                ind = groups.index(ride[1])
                offset = groups[:ind]
                rep = groups[ind:]
                break
            else:
                groups.append(ride[1])
                ride = (n, str(i%tam)+"-")
        i += 1
    return (sumQ(offset, queue), sumQ(rep, queue))

def themePark(tam, rides, queue):
    offset, rep = TPReps(tam, queue)
##    print "\n"
##    print offset
##    print rep
    money = 0
    if rides<= len(offset):
        money = sum(offset)
    else:
        of = 0
        money = money + sum(offset)
        money = money + ((rides-len(offset))/len(rep))*sum(rep)
        money = money + sum(rep[0:((rides-len(offset))%len(rep))])
    return money

def themeParkFB(tam, rides, queue):
    ind = 0
    money = 0
    for i in range(0,rides):
        slot = 0
        if tam<sum(queue):
            while slot<=tam:
                slot += queue[ind%len(queue)]
                ind = ind + 1
            ind = ind - 1
            slot -= queue[ind%len(queue)]
            money = money + slot
        else: 
            money = sum(queue)*rides
    return money

##1 4 2 1

file = open("C-small-attempt1.in", 'r')
cases = int(file.readline())
for case in range(0, cases):
    rides, tam, size = map(int, file.readline().split(" "))
    queue = map(int, file.readline().split(" "))
    money = themeParkFB(tam,rides,queue)
    print "Case #" + str(case+1) +": "+ str(money)
