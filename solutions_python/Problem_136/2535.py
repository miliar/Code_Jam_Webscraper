# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:44:16 2014

@author: vajepeya
"""

# Google Code Jam 2014 - Qualification

# B - Cookie clicker Alpha

inpfile = 'B-large.in'
outfile = 'B-large.out'

finp = open(inpfile, 'r')
fout = open(outfile, 'w')

T = finp.readline()
lines = finp.readlines()

i = 0
out_string = ''

for line in lines:
    C, F, X = map(float, line.split())

    cur_rate = 2.0
    lapsed_time = 0.0
    
    # Check between buying another factory & waiting until X cookies are generated
    while (((C / cur_rate) + (X / (cur_rate + F))) <= (X / cur_rate)):
        # Buy another factory        
        lapsed_time += C / cur_rate
        cur_rate += F
        continue
    
    # Else wait for X / cur_rate seconds more to get X cookies
    i += 1
    lapsed_time += (X / cur_rate)
    
    out_string += 'Case #' + str(i) + ': ' + str(lapsed_time) + '\n'
    
    
print out_string
fout.write(out_string)

finp.close()
fout.close()