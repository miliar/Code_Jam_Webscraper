'''
Created on May 6, 2011

Google Code Jam

user: philipbo

@author: Phil Bozak
'''
import time

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0]

fr = open(namefile+'.in', 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
numCases = int(lines[0])

output = ""
for z in range(numCases):
    cnt = 0
    st = lines[2*z+2]
    nums = [int(a) for a in st.split(' ')]
    for t in range(len(nums)):
        if not nums[t]==(t+1):
            tmp = nums[t]
            ind = (nums.index(t+1, t))+1
            nums[t] = t+1
            nm = tmp
            while not ind==nm:
                tmp = ind
                ind = nums.index(ind, t)+1
                nums[tmp-1] = tmp
                cnt = cnt+1
            print nums
            nums[nm-1] = nm
            cnt = cnt+2
    output = output + "Case #"+str(z+1)+": "+str(cnt)+".000000\n"

output = output[:-1]

fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()