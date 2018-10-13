from collections import Counter
#fi=open("A-small-attempt2.in",'r')#Input File
#fo=open("A-small-attempt2.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File
    
T=int(fi.readline())
for case in range(1,T+1,1):
	############################################
    n = int(fi.readline())
    arr = [fi.readline().strip() for i in range(n)]
    sts = ""
    ans = True
    cnts = []
    for i in range(n):
        temp = ""
        prev = "0"
        cnt = []
        for ch in arr[i]:
            if prev != ch:
                temp += ch
                prev = ch
                cnt.append(1)
            else:
                cnt[-1] += 1
        if i == 0:
            sts = temp
        elif sts != temp:
            ans = False
            break
        cnts.append(cnt)
    if ans is False:
        ans = "Fegla Won"
    else:
        ans = 0       
        for ch in range(len(sts)):
            temp = None
            for c1 in cnts:
                i = c1[ch]
                j = 0
                for c in cnts:
                    j += abs(c[ch]-i)
                if temp is None or temp > j:
                    temp = j
            ans += temp
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))
