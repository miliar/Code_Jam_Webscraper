fi=open("C-small-attempt2.in",'r')#Input File
#fi=open("C-large.in",'r')#Input File
#fi=open("C.in",'r')#Input File
fo=open("C-small-attempt2.out","w")#Output File
#fo=open("C-large.out","w")#Output File

def find(arr,flag,a,ba,b,bb,cnt,n,mx,last):
	if(cnt<n):
		for i in range(last+1,n):
			if flag[i]==0:
				flag[i]=1
				if b+arr[i]<=a-arr[i]:
					if a-arr[i]>mx and ba^arr[i]==bb^arr[i]:
						mx=a-arr[i]
					mx=find(arr,flag,a-arr[i],ba^arr[i],b+arr[i],bb^arr[i],cnt+1,n,mx,i)
				flag[i]=0
	return mx
			
T=int(fi.readline())
for case in range(1,T+1,1):
    num = int(fi.readline())
    arr = map(int, fi.readline().split())
    a = ba = 0
    flag=[]
    for i in arr:
    	a=a+i
    	ba=ba^i
    	flag.append(0)
    #mid=int(a/2)-1
    #print str(ba)+" "+str(a)
    ans = find(arr,flag,a,ba,0,0,0,num,-1,-1)
    if ans==-1:
    	fo.write("Case #"+str(case)+": NO\n")
    	#print "NO"
    else:
    	fo.write("Case #"+str(case)+": "+str(ans)+"\n")
    	#print ans
