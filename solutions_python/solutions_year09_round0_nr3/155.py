from itertools import *
def encode(l):
    return [(len(list(group)),name) for name, group in groupby(l)]

def gindex(c):
    return [x for x in range(n)]
n=input()

def fill(n):
    return (4-len(str(n)))*'0'+str(n)
def contains(s1,s2):
    if s2=='':
        return True
    if len(s1)<len(s2):
        return False
    if s1[0]==s2[0]:
        return contains(s1[1:],s2[1:])
    return contains(s1[1:],s2)
def nsub(s):
    if not contains(s,s1):
        return 0
    s=encode(s)
    ls=len(s)
    #print s
    arr=[] #i means position in s, j means position in str
    for i in range(l): arr.append([0]*ls)
    for i in range(ls):
        if s[i][1]=='w':
            arr[0][i]=s[i][0]%10000
    #print arr
    for i in range(1,l):
        for j in range(ls):
            if s[j][1]==s1[i]:
                arr[i][j]=(s[j][0]*sum([arr[i-1][x] for x in range(0,j)]))%10000
    #print arr
    return sum([arr[l-1][x] for x in range(ls)])%10000

s1='welcome to code jam'
l=19
for i in range(n):
    st=raw_input()
    s=''.join([x for x in st if x in s1])
    print 'Case #'+str(i+1)+': '+fill(nsub(s))
