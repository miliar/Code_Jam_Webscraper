#!/usr/bin/python
#!coding=utf-8


fo = open('A-large.in', 'rw+')
line = fo.readline()
case_num = int(line)

a = 1
po = open('out', 'w')
def output(res):
    global a
    po.write('Case #'+str(a)+': '+str(res)+'\n')
    a += 1

def parseCase():
    case = fo.readline()
    params = case.split(' ')
    maxShiness = int(params[0])
    people = list(params[1])
    num = 0; pos = 0
    extra = 0
    for i in people:
        if pos > maxShiness:
            break
        i = int(i)
        if pos > num and i > 0:
            extra += pos - num
            num = pos
        num += i
        pos += 1
    return extra

while case_num:
    output(parseCase())
    case_num -= 1

