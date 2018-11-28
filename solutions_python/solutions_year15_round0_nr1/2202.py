fi=open("A-small-attempt0.in",'r')#Input File
fo=open("A-small-attempt0.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File


T=int(fi.readline())
for case in range(1,T+1,1):
    ans=0
    ############################################
    smax, nums = fi.readline().split()
    smax = int(smax)
    nums = map(int, list(nums))

    cnt = 0
    for i in range(smax+1):
        #print cnt, ans
        if nums[i] > 0 and cnt < i:
            ans += i - cnt
            cnt += i - cnt
        cnt += nums[i]
    #print cnt, ans, "\n"        
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))    
