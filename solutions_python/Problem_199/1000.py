T = int(input())
for t in range(1,T+1):
    [s,k] = input().split()
    k = int(k)

    s = list(s)
    n=len(s)
    c = 0
    i=0
    #print(s)
    while i< n-k:
        if s[i]=='-':
            c+=1
            for j in range(k):
                if s[i+j]=='-':
                    s[i+j]='+'
                else:
                    s[i+j]='-'
            #print(s)
        i+=1
    s = s[n-k:]
    if '-' in s and '+' in s:
        print('Case #{}: {}'.format(t,'IMPOSSIBLE'))
    elif '+' in s:
        print('Case #{}: {}'.format(t,c))
    else:
        print('Case #{}: {}'.format(t,c+1))
