f = open('C:\Python27\B-small-attempt1.in', 'r')

ip = list(f)

temp3 = ip[0].rsplit()
test = int(temp3[0])
z=1


for i in range(test):
    r = 2
    t = 0
    for j in range(3):
        temp2 = ip[z].rsplit()
        c=float(temp2[0])
        f=float(temp2[1])
        x=float(temp2[2])
        
 #   print c,f,x
    
    temp = 2
    
    if x<=c:
        t= x/2
        print ( str("Case #"+str(i+1) + ": " + str(t)))
        
    else:
        buy = True
        
        while(buy !=False):
            
            t1 = x/r
            t2 = c/r + x/(r+f)
            
            if(t1<=t2):
                buy = False
                t=(t1)
            else:
                r =r + f
                t=t2
                buy = True
    
        #print ( str("Case #"+str(i+1) + ": " + str(sum(times))))
        #print r
        time=0
        while(temp!=r):
            time += c/temp
            temp += f
            
             
        print "Case #" + str(i+1) + ": " + str(time + t)    
    
    
    
    
    z+=1
        
    
    
   
           
    