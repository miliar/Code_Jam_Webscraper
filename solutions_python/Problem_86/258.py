fi=open("C-small-attempt0.in",'r')#Input File
#fi=open("C-large.in",'r')#Input File
#fi=open("C.in",'r')#Input File
fo=open("C-small-attempt0.out","w")#Output File
#fo=open("C-large.out","w")#Output File


T=int(fi.readline())
for case in range(1,T+1,1):
    n,l,h = map(int, fi.readline().split())
    c=map(int, fi.readline().split())
    ans="NO"
    for i in range(l,h+1):
    	flag=0
    	for j in range(n):
    		if not (c[j]%i==0 or i%c[j]==0):
    			flag=1
    			break
    	if flag==0:
    		ans=str(i)
    		break
    fo.write("Case #"+str(case)+": "+str(ans)+"\n")
    #print ans
