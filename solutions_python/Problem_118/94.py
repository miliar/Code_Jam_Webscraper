import sys

lst=[]

def pal(s):
    i=0
    j=len(s)-1
    while i<j:
        if (s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True

def go(s):
    if (len(s)>100):
        return
    v=int(s)
    v*=v
    if pal(str(v)):
        lst.append(v)

def rec(s):
    #too long?
    if len(s)>25:
        return
    #try it
    go(s+s[::-1])
    go(s+"0"+s[::-1])
    go(s+"1"+s[::-1])
    go(s+"2"+s[::-1])
    #add another digit
    rec(s+"0")
    if (s[0]=='1'):
        rec(s+"1")

#code to generate the list of palindromic squares (in advance)
#f = open('pal.txt','w')
#go("1")
#go("2")
#go("3")
#rec("1")
#rec("2")
#lst.sort()
#f.write(str(len(lst)))
#f.write("\n")
#for v in lst:
#    f.write(str(v))
#    f.write("\n")
#f.flush()
#f.close()
        
#code to solve the problem (using the generated file)
f = open('pal.txt','r')
vals=f.readlines()
f.close()

inp = open('in.txt','r')
out = open('out.txt','w')
t=1
for ln in inp:
    (A,B)=ln.split()
    A=int(A)
    B=int(B)
    cnt=0
    for v in vals:
        if len(v)>1:
            if (A<=int(v)) and (int(v)<=B):
                cnt+=1
            elif (int(v)>B):
                break
    out.write("Case #%d: %d\n" % (t,cnt))
    t+=1
out.close()