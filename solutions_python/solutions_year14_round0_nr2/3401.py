def getTime(cnt, rate, target):
    return (target-cnt)/rate

def getOptTime(C,F,X):
    cnt=0
    rate=2.000000
    time=0.0
    while True:    
        # test if target is reached before farm price
        if (X-cnt)/rate<=C/rate:
        # print("x1")
            return time + (X-cnt)/rate
            
        # otherwise: 
        else:
            time=time+C/rate
            cnt=C        
        # check for the critical point, where saving
        # cookies will be more rewarding than buying
        # farms
        if getTime(cnt, rate, X)<=getTime(0, rate+F, X):    
            return time+(X-cnt)/rate        
        else:
            # buy a farm
            #print("buy a farm")
            rate+=F


          
import os
import time
def load():
    print("starting...")
    t = time.clock()
    workdir  = os.path.join("C:\\\\","Users","olaf","CodeJam2014")
    file_name = "B-small-attempt0.in"
    #file_name = "CookieSample.txt"
    out_file_name = file_name.split(".")[0] + "_result." + file_name.split(".")[1]
    out = open(os.path.join(workdir, out_file_name), "w")
    file = open(os.path.join(workdir, file_name), "r")
    i=0        
    for line in file.read().splitlines():        
        a=line.split(" ")       
        if len(a)==3:
            i+=1
            vals=(list(map(float, a)))            
            result="Case #" + str(i)+ ": "+ str(round(getOptTime(vals[0],vals[1],vals[2]),7)) + "\n"
            print(result )
            out.write(result)
            
    print(time.clock() - t)
    out.close()
    file.close()
  
load()


##C=20 # farm price
##F=10 # additional rate
##X=100000 #cookie target
##
##C,F,X=30.0,1.0,2.0
##print(getOptTime(C,F,X))
##C,F,X=30.0,2.0,100.0
##print(getOptTime(C,F,X))
##C,F,X=30.50000,3.14159,1999.19990
##print(getOptTime(C,F,X))
##C,F,X=500.0,4.0,2000.0
##
##print(getOptTime(C,F,X))
##        
##    
##       
