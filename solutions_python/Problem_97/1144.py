def listint(n):
    if (n/10) == 0:
        return [n]
    else:
        return (listint(n/10)) + [(n%10)]

def intlist(l):
    if l==[]:
        return 0
    else:
        return (intlist(l[:-1])*10)+l[-1]

def belongs(x,l):
    if l==[]:
        return False
    elif x==l[0] :
        return True
    else:
        return belongs(x,l[1:])

def clean(l):
    if l==[]:
        return []
    elif belongs(l[0],l[1:]):
        return clean(l[1:])
    else:
        return [l[0]]+clean(l[1:])

def recs(n):
    nl = listint(n)
    siz = len(nl)
    ans = []
    i=0
    while (i<siz-1):
        nl = [nl[siz-1]]+nl[0:siz-1]
        ans = ans + [nl]
        i+=1
    ans = clean(ans)
    return map(lambda x:(n,intlist(x)),ans)

def rec (A,B):
    ans=[]
    n=A
    while(n<=B):
        ms=recs(n)
        goodms = filter ((lambda (y,x): (x>n and x<=B)), ms)
        ans = ans + goodms
        n += 1
    return len(ans)

i = open('input', 'r')
n = int((i.readline())[:-1])
j=0
il=[]
while(j<n):
    il = il+[((i.readline())[:-1])]
    j += 1

def inttup(s):
    s1=''
    s2=''
    while(s[0]!=' '):
        s1 = s1+s[0]
        s = s[1:]
    while(s!=''):
        s2 = s2+s[0]
        s = s[1:]
    return (int(s1),int(s2))

il=map(inttup, il)

def recycle (l):
    n = len(l)
    i=0
    ol = []
    while (i<n):
        t = "Case #"+str(i+1)+": "+str(rec(l[i][0],l[i][1]))
        ol = ol+[t]
        i += 1
    return ol

def show(l):
    if l==[]:
        return ""
    elif len(l)==1:
        return l[0]
    else:
        return l[0]+"\n"+show(l[1:])

print show(recycle(il))
