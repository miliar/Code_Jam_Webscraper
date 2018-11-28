import sys
n = int(input())

for i in range(n):
    d={}
    s,k=input().split()
    s=list(s)
    for j in range(len(s)):
        d[j]=s[j]
    c=0
    for j in range(len(d)):
        imp=False
        if d[j]!='-':
            pass
        else:
            for x in range(int(k)):
                try:
                    if d[j+x]=='+':
                        d[j+x]='-'
                    else:
                        d[j+x]='+'
                except:
                    imp=True
                    print("Case #{0}: {1}".format(i+1, 'IMPOSSIBLE'))
                    break
                    print('Hi')
            if imp==True:
                break
            c+=1
    if imp==False:
        print("Case #{0}: {1}".format(i+1, c))
