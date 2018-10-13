# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:13:24 2017

@author: Trevor
"""

class Horse():
    def __init__(self,input_line):
        self.pos = float(input_line.split(' ')[0])
        self.speed_init = float(input_line.split(' ')[1])

def solve(horses,num_horses,destination):
    i = num_horses - 1
    horses[i].stop_time = float(destination-horses[i].pos)/(horses[i].speed_init)
    while i > 0:
        i = i - 1
        horses[i].stop_time = max(float(destination-horses[i].pos)/(horses[i].speed_init),horses[i+1].stop_time)
    return destination/horses[0].stop_time

def run(filename):
    f = open(filename,"r")
    data = f.read()
    f.close()
    
    lines = data.splitlines()
    num_cases = int(lines[0])
    i = 1
    cases_run = 0
    answer_string = ""
    while cases_run < num_cases:
        line = lines[i]
        destination = int(line.split(' ')[0])
        num_horses = int(line.split(' ')[1])
        horses = [Horse(lines[j]) for j in xrange(i+1,i+1+num_horses)]
        answer = solve(horses,num_horses,destination)
        cases_run = cases_run + 1
        answer_string = '{}Case #{}: {}\n'.format(answer_string,cases_run,answer)
        i = i + 1 + num_horses
    out_file = filename.split('.')[0] + "_out.txt"
    f = open(out_file,"w")
    f.write(answer_string)
    f.close()