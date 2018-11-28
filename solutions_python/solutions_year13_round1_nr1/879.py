#!/usr/bin/env python3

line_number = 1

r,t = [],[]

r, t = [], []    
for l in open('A-small-attempt0.in', encoding='utf-8').readlines():
    if line_number == 1:
        problem_number = int(l.rstrip())
        line_number = 0
    else:
        data = l[:-1].split(' ')
        r += [int(data[0])]
        t += [int(data[1])]

for case in range(0,problem_number):
    num = 0
    area = 0
    n = 1

    while 1:
        tmp =  2 * (n + r[case]) - 1
        if area + tmp > t[case]:
            break
        area += tmp
        num += 1
        n += 2
    
    print('Case #',case+1,': ',num,sep='')
