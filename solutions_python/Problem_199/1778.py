res=[]

def solve(n):
    cont=0
    for a in range(len(n[0])):
        if n[0][a]=='-':
            if len(n[0])-a<int(n[1]):
                return "IMPOSSIBLE"
            else:
                l = list(n[0])
                for b in range(a,a+int(n[1])):
                    l[b]=inverte(l[b])
                n[0]=''.join(l)
                cont=cont+1
    return cont
    
    
            

def inverte(x):
    if x=='+':
        return '-'
    else:
        return '+'

def ver(x):
    for a in range(x):
        if x[a]=='-':
            return False
    return True

def separa(x):
    r1=""
    r2=""
    for a in x:
        if a==' ':
            pass
        elif a=='+' or a=='-':
            r1+=a
        else:
            r2+=a
    return [r1,r2]

i = int(input())
strings = []
for a in range(i):
    s = input()
    strings.append(separa(s))

res = "Case #%d: %s"

for a in range(i):
    print(res%(a+1, str(solve(strings[a]))))