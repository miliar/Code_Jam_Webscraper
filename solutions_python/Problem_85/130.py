fi=open("B-small-attempt0.in",'r')#Input File
#fi=open("B-large.in",'r')#Input File
#fi=open("B.in",'r')#Input File
fo=open("B-small-attempt0.out","w")#Output File
#fo=open("B-large.out","w")#Output File


T=int(fi.readline())
for case in range(1,T+1,1):
    arr = map(int, fi.readline().split())
    l=arr[0]
    t=arr[1]
    n=arr[2]
    c=arr[3]
    dist=[]
    j=0
    for i in range(n):
    	dist.append((arr[4+(j%c)]))
    	j+=1
    time=0
    s=0
    for i in range(n):
    	if dist[0]*2<=t-time:
    		 time+=dist[0]*2
    		 del(dist[0])
    	else:
    		dist[0]=dist[0]-((t-time)/2)
    		time=t
    dist.sort()
    for i in range(len(dist)-1,-1,-1):
    	if l!=0:
    		time+=dist[i]
    		l-=1
    	else:
    		time+=dist[i]*2
    #print time
    fo.write("Case #"+str(case)+": "+str(time)+"\n")
