#!/usr/bin/python
__author__ = 'Jin'

import sys
#sys.argv[0] input
#sys.argv[1] output file


#get the input data
#open the file
read = open(sys.argv[1],"r");
write = open(sys.argv[2],"w");
data = read.readlines()
read.close()

test_cases = data.pop(0)

result = range(int(test_cases))
for i in range(0,int(test_cases)):
    time = 0.0;
    cookie_rate = 2.0 ;
    cfx =data.pop(0).split()
    farm_cost = float(cfx[0]);
    farm_rate = float(cfx[1]);
    total_cookie = float(cfx[2]);
    
    while True:
        if(((total_cookie/(cookie_rate+farm_rate))+(farm_cost/cookie_rate))> total_cookie/cookie_rate):
            time += total_cookie/cookie_rate
            break
        time += (farm_cost/cookie_rate)
        cookie_rate += farm_rate

    write.write('Case #'+str(i+1)+': '+str(time)+"\n")
write.close()
