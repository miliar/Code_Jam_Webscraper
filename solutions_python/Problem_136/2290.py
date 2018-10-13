#from __future__ import Decimal
with open("test.in",'r') as r:
    dataset = r.readlines()
    r.close()

test_cases=int(dataset[0][:-1])
c= 0.0
x=0.0
f=0.0
rate =2.0

def wait(x,f):
    x1=x
    f1=f
    temp_time1=x1/float(f1)
    return temp_time1

def buy_wait(x,c,rate,f):
    x1=x
    c1=c
    f1=f
    r=rate
    cookies =0
    while True:
        #if x==100.0:
         #   print "b","c1:",c1,"x1:",x1,"r:",r
        #cookies += r
        #if cookies == c1:
        temp_time = c1/float(r)
        r += f1
        break
    temp_time_wait= temp_time + wait(x1,r)

    return temp_time,temp_time_wait
            
        


timer=0.0
with open("Output_gcj.txt",'w') as w:
    for i in range(1,test_cases+1):
        c,f,x = [float(k) for k in dataset[i][:-1].split()]
        #print c,f,x

        while True:
            #if f==2.0:
              #  print "a"

            t1,t2=buy_wait(x,c,rate,f)

            min_time =min(t2,wait(x,rate))
            if min_time == t2:
                rate += f
                timer += t1

            elif min_time == wait(x,rate):
                timer += wait(x,rate)
                w.write("Case #%d:" %(i) + " " + str(timer) + '\n')
                rate =2.0
                timer=0.0
                break

w.close() 
        
            
            
        

    
    
