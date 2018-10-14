class fly:
    R=0
    r=0
    t=0
    f=0
    g=0
    
            
            
    def readinput(self):
        import string
	import math

        file=open("C-small-attempt0.in",'r')
        p=file.readline()

        ansfile=open("C-small.out",'w')
        count1=int(p)
        k1=0
	A=0;
	B=0;
	P=0;
	
	#print 'g'
        while(k1<count1):
	    # here start the mess
	    k1=k1+1
	    g=file.readline()
            g=string.strip(g,None)
	    K=0;
	    K=int(g);
	    g=file.readline()
	    g=string.strip(g,None)
            arr=g.split(' ')
	    n=int(arr[0]);
	    l=[];
	    
	    for i in range(1,n+1):
		 l.append(int(arr[i]));   
		 #print arr[i]
	    #A=int(arr[0]);
	    #B=int(arr[1]);
	    #P=int(arr[2]);
	    
	    lk=[];
	    index=[];
	    for i in range(0,K):
		    lk.append(0);
		    index.append(i+1);
	    curr=-1;
	    ran=K;
	    new=-1
	    num=1;
	    for i1 in range(0,K):
		    new=(curr+num)%ran;
		    #print 'new ',new
		    #print 'index ',index
		    #print 'l ',lk
		    lk[index[new]-1]=lk[index[new]-1]+num;
		    #index.remove(new);
		    del index[new];
		    #if(new>curr):
	 	    new=new-1;
		    ran=ran-1;
		    
		    num=num+1;
		    curr=new;
		    
		    
		   
		   
	    #print 'lk ',lk	
	    #print l   
	    str1=""
            for i1 in l:
		   str1=str1+' '+str(lk[i1-1])
		   
		   
		   
		    
            #print i1
	    
	    
            ansfile.write("Case #"+str(k1)+":"+str1+"\n")
	    count=0
            
    
   
if __name__=="__main__":
    m=fly()
    m.readinput()
   