f=open("txt","r")
cases=int(f.readline())
i=0
while(1):
	clock=0
	arr1= f.readline().split()
   	C=float(arr1[0])
   	F=float(arr1[1])
   	X=float(arr1[2])
 	incr=2
        cks=0
        while(1):
		if(float(X)/incr>((float(C)/incr)+(float(X)/(incr+F)))):
			clock+=(C/incr)
			incr+=F
		else:
			break
	
        final_time=clock+float(X)/incr
        print "Case #"+str(i+1)+":",round(final_time,7)
        i+=1
	if(i==cases):
		break
 
         
