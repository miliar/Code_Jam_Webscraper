t = input()
for i in range(t):
    n,m = raw_input().split()
    s = list(map(int,list(m)))
    j = 1
    
    ans = 0
    num = s[0]
    while(j<len(s)):
        if(num<j and s[j]>0):
            c = j-num
            ans += c
            num+=ans
        num+=s[j]
        j+=1
    print("Case #%d: %d"%(i+1,ans))    
            
