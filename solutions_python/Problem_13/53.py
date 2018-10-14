class fly:
       
            
            
    def readinput(self):
        import string
	import math
##        print 'hi'
        file1=open("A-large.in",'r')#B-small-attempt0.inB-small-attempt1.inA-small-attempt0
        p=file1.readline()
	#print p
        ansfile=open("Alarge.out",'w')
        count1=int(p)
        k1=0
	#print 'gffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        while(k1<count1):
	    #print 'case ',k1
	    k1=k1+1
            p=file1.readline();
	    fg=p.split(' ');
	    M=int(fg[0]);
	    V=int(fg[1]);
	    Alist=[];
	    A0=[];
	    A1=[];
	    C=[];
	    for i in range(0,(M-1)/2):
		    p=file1.readline();
		    fg=p.split(' ');
		    Alist.append(int(fg[0]));
		    C.append(int(fg[1]));
		    A0.append(1000000);
		    A1.append(1000000);
	    for i in range((M-1)/2,M):
		    p=file1.readline();
		    fg=int(p);
		    Alist.append(int(fg));
		    C.append(0);
		    if fg ==0:
			    A0.append(0);
			    A1.append(1000000);
	  	    else :
			    A0.append(1000000);
			    A1.append(0);
	    #print Alist;
	    #print A0;
	    #print A1;
	    
	    j=(M-1)/2-1;
	    #print 'j',j
	    while j>=0:
		    #print Alist[j];
		    currA=Alist[j];
		    currC=C[j];
		    lc=(j+1)*2-1;
		    lr=(j+1)*2;
		    #if j !=0:
			    #lc=j*2;
			    #lr=j*2+1;
	            #else:
			    #lc=1;
			    #lr=2;
		    #print "j is",j," lc is",lc," lr is ",lr;
		    if currA == 1:
				if currC == 0:
					A1[j]=A1[lc]+A1[lr];
					A0[j]=min(A0[lc]+A0[lr],A1[lc]+A0[lr],A0[lc]+A1[lr]);
					#print "A1 is",A1[j];
				else:
					A1[j]=min(A1[lc]+A1[lr],A0[lc]+A1[lr]+1,A1[lc]+A0[lr]+1);
					#print 'A1[j] is ',A1[j];
					A0[j]=min(A0[lc]+A0[lr],A1[lc]+A0[lr],A0[lc]+A1[lr]);
		    else:
				    if currC == 0:
					A1[j]=min(A1[lc]+A1[lr],A1[lc]+A0[lr],A0[lc]+A1[lr]);
					A0[j]=A0[lc]+A0[lr];
					#print 'selected ',A0[j];
					#print 'selected ',A1[j];
				    else:
					A1[j]=min(A1[lc]+A1[lr],A1[lc]+A0[lr],A0[lc]+A1[lr]);
					A0[j]=min(A0[lc]+A0[lr],A1[lc]+A0[lr]+1,A0[lc]+A1[lr]+1);
				    
		    #print "j is ",j;		  
		    #print "Alist is",Alist;
		    #print "C is",C;
		    #print "A0 is",A0;
		    #print "A1 is",A1
		    
		    j=j-1;
		    
	    ans='';
	    #print "Alist is  ",A0
	    #print 'ans is';
	    if V == 0:
	    	if A0[0]>=1000000 :
			#print 'impossible'
			ans='IMPOSSIBLE'
		else :
			#print A0[0];
			ans=str(A0[0])
	    else:
		    if A1[0]>=1000000 :
			ans='IMPOSSIBLE';
			#print 'impossible'
		    else :
			ans=str(A1[0]);
			#print A1[0];
	    
	    
	    
	    
	    ansfile.write("Case #"+str(k1)+": "+ans+"\n")
	    count=0
            
      
if __name__=="__main__":
    m=fly()
    m.readinput()
    #l=[[0,0],[1,0],[1,1],[1,0]]
    #[0,0],[1,0],[1,1],[1,0]
##    print m.getAreaC([0,0],[3,0],)
##    print m.getArea([2,2],[6,2],[6,6],[2,6],3.0)
    
