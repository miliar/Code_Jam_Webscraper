fi=open("C-small-attempt0.in",'r')#Input File
fo=open("C-small-attempt0.out",'w')#Output File

#fi=open("C-large.in",'r')#Input File
#fo=open("C-large.out","w")#Output File
ans = 0

#fi=open("C.in",'r')#Input File
#fo=open("C.out","w")#Output File


def find(a,b,n,m,x,t,check, xyz):
    global ans    
    #print "%s-->%s"%(x,t)
    if n==x or m==t:
        ans = max(ans, check)
        #print ans
        #print xyz
        return
        
    find(a,b,n,m,x+1,t,check, xyz)
    
    bn = a[2*x]
    bc = a[2*x+1]
    
    done = False
    for i in range(t, m, 1):
        tn = b[2*i]
        tc = b[2*i+1]
        if bc==tc:
            red = min(bn,tn)
            a[2*x] -= red
            b[2*i] -= red
            
            if bn==tn:
                find(a,b,n,m,x+1,i+1,check+red, xyz+[(x+1,i+1)])
            elif bn==red:
                find(a,b,n,m,x+1,i,check+red, xyz+[(x+1,i+1)])
            else:
                find(a,b,n,m,x,i+1,check+red, xyz+[(x+1,i+1)])
            
            a[2*x] += red
            b[2*i] += red
            
            break
            

T=int(fi.readline())
for case in range(1,T+1,1):
	ans=0
	############################################
	n, m = map(int, fi.readline().split())
	a = map(int, fi.readline().split())
	b = map(int, fi.readline().split())
	
	
	find(a,b,n,m,0,0,0, [])
	print "%s %s"%(case, ans)
	############################################
	fo.write("Case #%s: %s\n"%(case, ans))


    
    
