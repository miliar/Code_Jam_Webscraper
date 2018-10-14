# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:19:07 2017

@author: Bredock
"""

file = "G:\Programming\Google Jam\Day3\A-large.in"
file_out = "G:\Programming\Google Jam\Day3\A-large.out"
f = open(file)
g = open(file_out, "w")
cases = f.readline()

num_case = 0
for i in range(1,int(cases)+1):
    meta, num_horses = f.readline().split()
    horses = []
    times = []
    for j in range(int(num_horses)):
        horse_temp = f.readline()   
        horse_temp = horse_temp.split()
        horses.append(horse_temp)
        time_horse = (float(meta) - float(horse_temp[0])) / float(horse_temp[1])
        times.append(time_horse)
    num_case += 1
    time_total = float(meta) / max(times)
    g.write("Case #"+str(num_case)+": "+str(time_total)+"\n")
g.close()