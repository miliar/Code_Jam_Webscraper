T = int(input())
for t in range(1,T+1):
    s = list(input())
    #print(s)
    i = 1;
    while i<len(s) and s[i]>=s[i-1]:
        i+=1
    #print(i)
    if i==len(s):
        print('Case #{}: {}'.format(t,''.join(s)))
    else:
        for j in range(i,len(s)):
            s[j]='9'
            #print(j)
        #print(s)
        s[i-1]=chr(ord(s[i-1])-1)
        i-=1
        #print(i)
        while i>0 and s[i]<s[i-1]:
            s[i]='9'
            s[i-1]=chr(ord(s[i-1])-1)
            i-=1
        i=0
        while s[i]=='0':
            i+=1
        print('Case #{}: {}'.format(t,''.join(s[i:])))
