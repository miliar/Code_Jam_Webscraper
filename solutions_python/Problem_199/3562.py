t=int(input())
r=[]
for i in range(t):
    s,k=input().split()
    s=list(s)
    k=int(k)
    b=0
    for j in range(len(s)):
        if s[j]=='-':
            if j+k>len(s):
                break
            else:
                b+=1
                for l in range(j,j+k):
                    if s[l]=='-':
                        s[l]='+'
                    else:
                        s[l]='-'             
    if '-' in s:
        r.append('IMPOSSIBLE')
    else:
        r.append(b)
for i in range(len(r)):
    print('Case #',i+1,':',' ',r[i],sep='')
                    
        
    