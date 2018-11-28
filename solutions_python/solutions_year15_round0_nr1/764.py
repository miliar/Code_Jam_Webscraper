
f=open("/tmp/A-large.in","r")
g=open("/home/akshay/Desktop/codejam11.txt","w")
       

    
t=f.readline()
t=int(t)


#if t>=1 and t<=100:
test=0
#print test

while t>0:
        
    suml=0
    count2=0
    test=test+1
    #print sum
    var=f.readline()
    #print var
    n,ml=var.split()
    n=int(n)
    ml=str(ml)
    ml=list(ml)
    for k in ml:
        k=int(k)
        #print n, ml
        
    for i,j in enumerate(ml):
        count=0

        if i>0:
            suml=suml+int(ml[i-1])

            if suml<i:
                count=count+(i-suml)
                count2=count2+count
                ml[i]=int(ml[i])+ count
              
    result= str("Case #"+str(test)+str(":"))
    #print result
    g.write(result+" "+str(count2))
    g.write("\n")
    t=t-1
f.close()
g.close()
    

