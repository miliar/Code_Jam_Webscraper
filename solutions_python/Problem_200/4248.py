testcases=input()
def is_not_sorted(l):
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
            pass
        else:
            return True
    return False

def update(l):
    for i in range(len(l)-1):
        if (l[i]>l[i+1]):
            p=int(l[i])
            p=p-1
            c=len(l)-i
            l=l[0:i]+[str(p)]+['9' for i in range(c-1)]
    return l
            
for t in range(testcases):
    N=int(raw_input())
    Nl=[i for i in str(N)]
    while is_not_sorted(Nl) and N>0:
        Nl=update(Nl)
    s=''.join(Nl)
    if s[0]=='0':
        print("Case #"+str(t+1)+': '+str(s[1:]))
    else:
        print("Case #"+str(t+1)+': '+str(s))
