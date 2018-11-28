#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

fin = open("d:/google/B-small-attempt0.in")
fout = open("d:/google/B-small-attempt0.out", "w")
num_test_cases = fin.readline()
result_list = []
for i in xrange(1, int(num_test_cases) + 1):
    case_num = "Case #%d: "%i
    price, extra, obj = [float(i) for i in fin.readline().strip().split(' ')]
    t_cum = 0
    speed = 2.0
    while True:
	t1 = obj / speed 
	t2 = price / speed
	t3 = t2 + obj / (speed + extra)
	if t1 <= t3:
	    t_cum += t1
	    break
	else:
	    t_cum += t2
	    speed += extra
    result_list.append(case_num + str(round(t_cum, 7)))
fout.writelines('\n'.join(result_list))
	    
