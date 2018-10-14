t=int(raw_input())
jj=1
while t>0:
    s=list((raw_input()))
    if len(s)>1:
        i=1
        while i<len(s):
            if s[i]<s[i-1]:
                if s[i]=='0':
                    if s[i-1]=='1':
                        s[0]='0'
                        for j in range(1,i):
                            s[j]='9'
                    else:
                        while(i>1 and s[i-1]==s[i-2]):
                            i-=1
                        s[i-1]=str(int(s[i-1])-1)
                    for j in range(i,len(s)):
                        s[j]='9'
                else:
                    while(i>1 and s[i-1]==s[i-2]):
                            i-=1
                    s[i-1]=str(int(s[i-1])-1)
                    for j in range(i,len(s)):
                        s[j]='9'                    
                break
            i+=1
    print("Case #"+str(jj)+": "+str(int(''.join(s))))
    jj+=1
    t-=1
