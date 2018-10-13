fi=open("B-small-attempt0.in",'r')#Input File
fo=open("B-small-attempt0.out",'w')#Output File

#fi=open("B-large.in",'r')#Input File
#fo=open("B-large.out","w")#Output File

#fi=open("B.in",'r')#Input File
#fo=open("B.out","w")#Output File
    
T=int(fi.readline())
for case in range(1,T+1,1):
	############################################
    a, b, k = map(int, fi.readline().split())
    ans = 0                        
    for i in range(a):
        for j in range(b):
            temp = i&j
            if temp < k:
                ans += 1
    #print ans               	
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))
