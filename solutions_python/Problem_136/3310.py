# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:32:55 2014

@author: Pam
"""


output_f = open('CC_output.txt', 'a')
with open('B-large.in', 'r') as f:
    num_cases = int(f.readline())
#    f.seek(0)
    for num, row in enumerate(f):
        case_num = str(num+1)
        total_cookies = 0
        cookie_rate = 2
        current_time = 0
        data = row.split()
        data= [float(i) for i in data]
        C = data[0]
        F = data[1]
        X = data[2]
        time_chunk = 0
        win_time =0
        while True:       
            if C>= X:
                win_time= X/cookie_rate
                break
            else:
                time_chunk = C/cookie_rate
                wait_time = X/cookie_rate
                next_farm_time = X/(cookie_rate+F)+time_chunk
                if wait_time <= next_farm_time:
                    win_time+=wait_time
                    break
                else:
                    cookie_rate+=F
                    win_time+=time_chunk
        print 'Case #'+case_num+': '+str(win_time)
        line_out ='Case #'+case_num+': '+str(win_time)+'\n'
        output_f.write(line_out)
            
                    
            
#            current_time+=.0001
#            total_cookies+=.0001*cookie_rate
#            wait_time = (X-total_cookies)/cookie_rate
#            next_farm_time = (X-total_cookies-C)/(cookie_rate+F)
#            if total_cookies >= X:
#                print current_time, 'on the mark'
#                break
#            elif wait_time <= next_farm_time:
#                print current_time+wait_time, 'wait time'
#                break
#            elif total_cookies>=C:
#                total_cookies = 0#total_cookies - C
#                cookie_rate+=F

#        print case_num, C, F, X
            

            