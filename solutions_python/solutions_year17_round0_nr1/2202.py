def flip(s,k,start):
    l = ""
    for i in range(len(s)):
        if(i >= start and i < start+k):
            if(s[i]=='+'):
                l+='-'
            else:
                l+='+'
        else:
            l+=(s[i])
    return l
for T in range(int(raw_input())):
    s,k = raw_input().split()
    k = int(k)
    n = len(s)
    count = 0
    for i in range(n - k + 1):
        if(s[i]=='+'):
            continue
        s = flip(s,k,i)
        count+=1
        #print(s+" df ")
    ans = str(count)
    if('-' in s):
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(T+1,ans))