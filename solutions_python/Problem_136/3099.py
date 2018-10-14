# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 00:22:53 2014

@author: Βίκυ!
"""
#%%
fin = open('C:/Users/Βίκυ!/Desktop/GoogleCodeJam/CookieClickerAlpha/RealDataSmall/input.txt', 'r')
fout = open('C:/Users/Βίκυ!/Desktop/GoogleCodeJam/CookieClickerAlpha/RealDataSmall/output.txt','w')
cases = int(fin.readline())
r = 2
for i in range(cases):
    totaltime = 0.0
    r = 2 #cookies per sec
    c,f,x = [float(x) for x in fin.readline().strip().split()]    
    time1 = x/r #just wait
    time2 = c/r + x/(f+r) #buy a farm and wait
    while time1>time2: #let's buy a farm!
        totaltime+=c/r
        r+=f
        time1 = x/r
        time2 = c/r + x/(f+r)
    totaltime = totaltime + time1 
    fout.write('Case #{}: {}\n'.format(i+1,round(totaltime,7)))
fin.close()
fout.close()
    