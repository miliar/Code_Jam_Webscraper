class fly:
    R=0
    r=0
    t=0
    f=0
    g=0
    
            
            
    def readinput(self):
        import string
	import math
##        print 'hi'
        file=open("C-small-attempt0.in",'r')#B-small-attempt0.inB-small-attempt1.in
        p=file.readline()
	#print p
        ansfile=open("C-small.out",'w')
        count1=int(p)
        k1=0
	#print 'gffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        while(k1<count1):
	    k1=k1+1
            p=file.readline()
	    fa=p.split(' ')
	    global f
	    global R
	    global t
	    global r
	    global g
            f=float(fa[0])
	    R=float(fa[1])
	    t=float(fa[2])
	    r=float(fa[3])
	    g=float(fa[4])
	    	    
            print 'f:',f,' R:',R,' t:',t,' r:',r,'  g:',g
            ans=0.0;
	    if 2*f>=g:
		    ans=0.0
	    else:
		    l=[]
		    x=0
		    y=0
		    x=x+r+f
		    y=y+r+f
		    while y<(R-t-f):
                            x=0+r+f
			    while x<(R-t-f):
##                                    print 'x ;',x,' y:',y
				    if self.dist([x,y],[0,0])<(R-t-f):
					    l.append([[x,y],[x+g-2*f,y],[x+g-2*f,y+g-2*f],[x,y+g-2*f]])
					    #print l
			            x=x+2*r+g
			    y=y+2*r+g
##			    print y
                    #print 'l is ',l
	    
		    for d in l:
                            hj=self.getArea(d[0],d[1],d[2],d[3],R-t-f)
                            print 'd  ',d,'  hj ',hj
			    ans=ans+hj
			    
			    
		    ans=ans*4
            pstr=((math.pi*(R)*(R))-ans)/(math.pi*(R)*(R))
	    print pstr
	    pstrt="%.6f" %pstr
            ansfile.write("Case #"+str(k1)+": "+pstrt+"\n")
	    count=0
            
    def getArea(self,x1,x2,x3,x4,radius):
	    if self.dist(x3,[0,0])<=radius:
		    return (x2[0]-x1[0])*(x2[0]-x1[0])
	    elif self.dist(x4,[0,0])<radius and self.dist(x2,[0,0])<radius:
		    #print 'hehe'
		    temp=self.getP(x4,x3,radius)		    
		    jkl=0.0
		    jkl=jkl+self.getAreaC(temp,x2,radius,x1)
		    jkl=jkl+self.getAreaR(x1,temp)
		    return jkl
            elif self.dist(x4,[0,0])<radius:
		    temp1=self.getP(x4,x3,radius)
		    temp2=self.getP(x1,x2,radius)
		    fgh=self.getAreaR(x1,temp1)
		    fgh=fgh+self.getAreaC(temp1,temp2,radius,x1)
		    return fgh
		    		                 
	    elif self.dist(x2,[0,0])<radius:
		    return self.getAreaC(x1,x2,radius,x1)    
		    
            else :              
                    print 'atleast this is right'
		    temp=self.getP(x1,x2,radius)
		    print x1,temp
		    #print x1,temp
		    return self.getAreaC(x1,temp,radius,x1)
		    
		 
    def getAreaR(self,x1,x2):
	    return (x2[0]-x1[0])*(x2[1]-x1[1])
    
    def getAreaCir(self,x1,x2):
	    import math
	    return math.pi*(x2[0]-x1[0])*(x2[0]-x1[0])
    
    def getAreaC(self,x1,x2,radius,base):
	    import math
##	    print 'yiu',radius
##	    print  math.asin(x2[0]/radius)
##	    print (radius*radius)*math.asin(x2[0]/radius)/2
##	    print x1,x2
	    gj=x2[0]*math.sqrt((radius*radius)-x2[0]*x2[0])/2+(radius*radius)*math.asin(x2[0]/radius)/2
##	    print x1[0]*math.sqrt((radius*radius)-x1[0]*x1[0])/2#+
	    print gj
	    print x1[0]*math.sqrt((radius*radius)-x1[0]*x1[0])/2+(radius*radius)*math.asin(x1[0]/radius)/2
	    print base[1]*(x2[0]-x1[0])

	    gj=gj-(x1[0]*math.sqrt((radius*radius)-x1[0]*x1[0])/2+(radius*radius)*math.asin(x1[0]/radius)/2)-base[1]*(x2[0]-x1[0])
	    print gj
	    return gj
    
    def getP(self,x1,x2,radius):
	    import math
	    #print x1
	    return [math.sqrt(radius*radius-x1[1]*x1[1]),x1[1]]
    
    def dist(self, l1,l2):
	     import math
	     return math.sqrt((l1[0]-l2[0])*(l1[0]-l2[0])+(l1[1]-l2[1])*(l1[1]-l2[1]))  
   
if __name__=="__main__":
    m=fly()
    m.readinput()
    #l=[[0,0],[1,0],[1,1],[1,0]]
    #[0,0],[1,0],[1,1],[1,0]
##    print m.getAreaC([0,0],[3,0],)
##    print m.getArea([2,2],[6,2],[6,6],[2,6],3.0)
    
