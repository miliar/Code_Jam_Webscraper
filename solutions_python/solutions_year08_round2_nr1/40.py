class fly:

    
            
            
    def readinput(self):
        import string
	import math

        file=open("A-small-attempt0.in",'r')
        p=file.readline()

        ansfile=open("smallA.out",'w')
        count1=int(p)
	#print count1
        k1=0
	#print 'g'
	n=0l;
    	A=0l; 
        B=0l; 
        C=0; 
        D=0;
        x0=0;
        y0=0; 
        M=0;
        while k1<count1 :
	    # here start the mess
	    k1=k1+1;
	    g=file.readline()
            g=string.strip(g,None)
            arr=g.split(' ')
	    count=0
	    #print arr;
	    n=int(arr[0]);
	    A=int(arr[1]) 
	    B=int(arr[2]);
	    C=int(arr[3]);
	    D=int(arr[4]);
	    x0=int(arr[5]);
	    y0=int(arr[6]);
	    M=int(arr[7]);
	    X = x0;
	    Y = y0;
	    l=[];
	    l.append([X,Y])
	    #if X%3==0:
		    #if Y%3==0:
			    #l[0]=l[0]+1;
		    #else if Y%3==1:
			    #l[1]=l[1]+1;
	    	    #else if Y%3==2:
			    #l[2]=l[2]+1;
	    #else if X%3==1:
		    #if Y%3==0:
			    #l[3]=l[3]+1;
		    #else if Y%3==1:
			    #l[4]=l[4]+1;
	    	    #else if Y%3==2:
			    #l[5]=l[5]+1;
	    #else if X%3==2:
		    #if Y%3==0:
			    #l[6]=l[6]+1;
		    #else if Y%3==1:
			    #l[7]=l[7]+1;
	    	    #else if Y%3==2:
			    #l[8]=l[8]+1;
			    
			   
	    #print X, Y
 	    for i in range( 0 , n-1):
		    X = (A * X + B)% M;
  	    	    Y = (C * Y + D)% M;
		    l.append([X,Y])
		    #print l
  	            #if X%3==0:
			#if Y%3==0:
				#l[0]=l[0]+1;
			#else if Y%3==1:
				#l[1]=l[1]+1;
			#else if Y%3==2:
				#l[2]=l[2]+1;
			#else if X%3==1:
					#if Y%3==0:
						#l[3]=l[3]+1;
					#else if Y%3==1:
						#l[4]=l[4]+1;
					#else if Y%3==2:
						#l[5]=l[5]+1;
			#else if X%3==2:
					#if Y%3==0:
						#l[6]=l[6]+1;
					#else if Y%3==1:
						#l[7]=l[7]+1;
					#else if Y%3==2:
						#l[8]=l[8]+1;
		
	    lg=len(l)
	    #print 'lg',lg
	    count =0;
	    for i1 in range(0,lg):
		    for j1 in range(i1+1,lg):
			    for k3 in range(j1+1,lg):
				    #print l[i1],'  ',l[j1],'  ',l[k1];
				    if ((l[i1][0]+l[j1][0]+l[k3][0])/3*3==(l[i1][0]+l[j1][0]+l[k3][0])) and ((l[i1][1]+l[j1][1]+l[k3][1])/3*3==(l[i1][1]+l[j1][1]+l[k3][1])):
					    #print 'i am here'
					    count=count+1;
	    
	    
            ansfile.write("Case #"+str(k1)+': '+str(count)+"\n")
	    #print k1," ",count1
            
    
   
if __name__=="__main__":
    m=fly()
    m.readinput()
   