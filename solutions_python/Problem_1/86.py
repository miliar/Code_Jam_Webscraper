class search:
    eng=[];
    quer=[];
            
            
    def readinput(self):
        import string
##        print 'hi'
        file=open("A-large.in",'r')
        p=file.readline()
	print p
        ans=open("large.out",'w')
        count1=int(p)
        k1=0
	#print 'gffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        while(k1<count1):
            self.eng=[];
            self.quer=[];
            
            k1=k1+1
	    p=file.readline()
	    p.strip(' ')
	    #print 'p is', p
            noEng=int(p)
	    i=0
	    while i<noEng:
		    self.eng.append(file.readline())
		    i=i+1
	    noQuer=int(file.readline())
	    i=0
	    while i<noQuer:
		    self.quer.append(file.readline())
		    i=i+1
            
            
	    templ=[]
	    for d in self.eng:
		    templ.append(d)
	    
	    k=0
	    count=0
	    while len(self.quer)!=0:
		q=self.quer.pop(0)
		#print 'quer is ',q
		#print 'templ is ',templ
		#print 'eng is',self.eng
		flag=1
		if len(templ)==1 and q in templ:
			count=count+1
			s=templ.pop(0)
			#print 'removing ',s
			for d in self.eng:
		           templ.append(d)
			templ.remove(s)
			#print 'templ has become ',templ
			flag=0
			
		if q in templ and flag==1:			
			templ.remove(q)
		        #print 'after removing ',q,'templ has become ',templ
		
			    
			    
		     
            ans.write("Case #"+str(k1)+": "+str(count)+"\n")
	    count=0
            
   
if __name__=="__main__":
    m=search()
    m.readinput()
