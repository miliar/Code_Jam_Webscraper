from collections import  namedtuple
from  heapq import *


templ = '/home/tocarip/Downloads/ProgrammingAssignment4Files/'

file_gr = open(templ+'qaz')

ln = file_gr.readlines()

num_cases = int(ln[0])

for j,l in enumerate(ln[1:]):
    k,a = l.split()
    res = 0
    cur_s  = 0
    for i,digit in enumerate(a):
        if i > cur_s and int(digit) != 0:
            res = res + (i -cur_s)
            cur_s = i+ int(digit)
        else:
            cur_s = cur_s + int(digit)
    print 'Case #'+ str(j+1) +  ': ' + str(res)
