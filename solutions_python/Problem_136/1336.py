import re
f = open('B-large.txt')
ff = open('outputB-large-attempt0.txt','w')

a = [set()] * 4
b = [set()] * 4

T = int(f.readline())
for ii in range(T):
    x = f.readline().split()
    C = float(x[0])
    F = float(x[1])
    X = float(x[2])
    if(C>=X):
        ff.write('Case #'+str(ii+1)+': '+str('%.7f'%(X/2))+'\n')
    else:
        time2 =  time=  float(0)
        rate = 2
        time1 = X/rate
        
        while(True):
            time2 += C/rate
            rate +=F
            time = X/rate
            time2 += time
            #print(time1,time2,rate,time)
            if(time1<time2):
                break
            time1 = time2
            time2 -= time
        ff.write('Case #'+str(ii+1)+': '+str('%.7f'%time1)+'\n')
f.close()
ff.close()
