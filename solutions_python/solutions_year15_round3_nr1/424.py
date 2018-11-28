__author__ = 'Reuben'
import math



def solution(r,c,w):
    ways = math.ceil(c/w)
    print(ways)
    ways *= r
    print(ways)
    ways += w-1
    print(ways)
    return ways


f_in = open('file.in')
f_out = open('file.out','w')

cases = int(f_in.readline()) #first line is always number of cases
for i in range(1,cases+1):
    l = f_in.readline().split()
    r = int(l[0])
    c = int(l[1])
    w = int(l[2])
    print(r,c,w)
    s = solution(r,c,w)
    f_out.write("Case #"+str(i)+": "+str(s)+"\n")

