maps = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

def f(c):
    return (maps[ord(c)-97])

def conv (s):
    if s=="":
        return ""
    elif s[0] == ' ':
        t = conv(s[1:])
        return " "+t
    else:
        t = conv(s[1:])
        return f(s[0])+t

i = open('input', 'r')
n = int((i.readline())[:-1])
j=0
l=[]
while(j<n):
    l = l+[((i.readline())[:-1])]
    j += 1

def convert (l):
    n = len(l)
    i=0
    ol = []
    while (i<n):
        t = "Case #"+str(i+1)+": "+conv(l[i])
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

print show(convert(l))
