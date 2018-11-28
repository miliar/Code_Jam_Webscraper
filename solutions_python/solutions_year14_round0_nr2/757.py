import math
import pdb


def check(C,F,X):
    rate = 2
    cookies = 0.0 #current
    time = 0.0   #current
    while True:
        projected_time = (X-cookies)/rate + time
        projected_upgrade_time = (C-cookies)/rate + time
        projected_time_with_upgrade= (X-0.0)/(rate+F) + projected_upgrade_time
        if projected_time < projected_time_with_upgrade:
            return projected_time
        cookies = 0
        time = projected_upgrade_time
        rate += F
##    //C = m*(x-t_prev)+C_prev
##    x - t_prev = (C - C_prev)/m
##    x = (X - C_prev)/m+t_prev #when I will reach targ
##    x = (C - C_prev)/m+t_prev #when I will reach cost
##    x = (X - C_new_prev)/m+t_new_prev #when I will reach targ with an upgrade
    


infile = open('B-large.in','r')
outfile = open('out.txt','w')
T = int(infile.readline())
for t in range(T):
    C,F,X = [float(a) for a in infile.readline().split(' ')]
    val = check(C,F,X)
    outfile.write('Case #'+str(t+1)+': {0:.7f}'.format(val)+'\n')
    print 'Case #'+str(t+1)+': {0:.7f}'.format(val)
        
infile.close()
outfile.close()
print 'Completed'
                
            
