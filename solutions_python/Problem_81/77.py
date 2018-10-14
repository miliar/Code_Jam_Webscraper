#fi=open("A-small-attempt1.in",'r')#Input File
fi=open("A-large.in",'r')#Input File
#fi=open("A.in",'r')#Input File
#fo=open("A-small-attempt1.out","w")#Output File
fo=open("A-large.out","w")#Output File

def cal(s):
	w=s.count("1")
	l=s.count("0")
	return(float(w)/float(w+l))
T=int(fi.readline())
for case in range(1,T+1,1):
    fo.write("Case #"+str(case)+":\n")
    n = int(fi.readline())
    ar=[]
    for i in range(n):
		ar.append(fi.readline())
    x=[]
    y=[]
    z=[]
    sm=0
    for i in range(n):
    	rpi=0  
    	wp=cal(ar[i])
    	x.append(wp)
    	owp=0.0
    	cn=0
	for j in range(n):
                if(i!=j and ar[j][i:i+1]!="."):
			owp+=cal((ar[j][:i]+ar[j][i+1:]))
			cn+=1
	owp=owp/float(cn)
	#print "owp:"+str(owp)
	sm+=owp
	y.append(owp)
    #print "sum:"+str(sm)
    for i in range(n):
        ind=ar[i].find(".")
        v=sm
        while(ind>=0):
             v-=y[ind]
             ind=ar[i].find(".",ind+1)
        v=float(v)/float(n-ar[i].count("."))
        #print "--"+str(sm-y[i])+" "+str(n-ar[i].count("."))
    	rpi=0.25*x[i]+0.50*y[i]+0.25*v
    	fo.write(str(rpi)+"\n")
    	#print rpi
