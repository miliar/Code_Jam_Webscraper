
# coding: utf-8

# In[1]:

import sys


# In[2]:

from __future__ import print_function


# In[3]:

def get_min_time(cake_list):
    min_time = sys.maxint
    n = max(cake_list)
    for n in range(1, max(cake_list)+1):
        # get time to split
        time_to_split = 0
        for cake_num in cake_list:
            time_to_split += int((cake_num - 1)) / n
        # get total time
        total_time = time_to_split + n
        # get min_time
        min_time = min(total_time, min_time)
    return min_time


# In[4]:

case_ind = 0
line_ind = 0
f_out = open('B-large.out','w')
with open('B-large.in') as f:
    for line in f:
        # ignore first line and odd line
        if line_ind == 0 or line_ind % 2 == 1:
            line_ind += 1
            continue;
        # read even line
        case_ind += 1
        line_ind += 1
        cake_list = map(int, line.strip().split())
        # print cake_list
        print ("Case #" + str(case_ind) + ": " + str(get_min_time(cake_list)), file=f_out)
f_out.close()


# In[ ]:



