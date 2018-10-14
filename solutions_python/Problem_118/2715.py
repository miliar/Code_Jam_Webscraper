import math

f = open('/home/dexter/input1.in', 'r')

cases = int(f.readline())


for k in range (0, cases):
    a = f.readline()
    itms=a.split()
    out=0
    for i in range(int(itms[0]),int(itms[1])+1):
        x=str(i)
        y =x[::-1]
        if(y==x):
             x=int(x)
             if((math.sqrt(x)-int(math.sqrt(x))) == 0):
                 x=str(int(math.sqrt(x)))
                 y =x[::-1]
                 if(y==x):
                      out+=1
                     
                
            
              
     
     
   

    print "Case #"+str(k+1)+": "+str(out)
