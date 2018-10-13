# cook your dish here
t=int(input())
def flip(s,i,k):
    for w in range(i,i+k):
        if s[w]=='+':
            s[w]='-'
        elif s[w]=='-':
            s[w]='+'
    return s
for ui in range(t):
    s,k=input().split()
    k=int(k)
    print("Case #",ui+1,": ",sep='',end='')
    if s.count('+')==len(s):
        print('0')
    else:
        p=list(s)
        d=0
        for i in range(len(p)-k+1):
            if p[i]=='-':
                p=flip(p,i,k)
                d+=1
        s=''.join(p)
        if s.count('+')==len(s):
            print(d)
        else:
            print('IMPOSSIBLE')
        
    