f1=open("B-small-attempt3.in","r")

t=f1.readline()

t=int(t)
fl=1
j=0
list=[]
for i in xrange(t):
    n=f1.readline()
    n=int(n)	
    k=n	
    while 	(k>=1):
        j=k	
        fl=1		
        while((j/10)>0):
            a=j%10
            			
            j=j/10
            b=j%10
            #print a,b,j  			
            if b>a:
                fl=0 			
                break
        if fl==1:
            list.append(k)		
            break 	
        k=k-1			
f2=open("1122.txt","w")
for i in xrange(t):
    f2.write("Case #")
    f2.write(str(i+1))
    f2.write(": ")  	
    f2.write(str(list[i]))
    f2.write("\n")	
