import math


def demo():
    a=open("C-small.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        res=check(int(b[i*2+1].split()[1])*b[i*2+2][:-1])
        #res=check(b[i+1].split()[1])
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

def check(r1):
    r=r1.replace('i','2').replace('j','3').replace('k','4')
    if r=='2'*len(r) or n(r)!=-1:
        return 'NO'
    for x in range(1,len(r1)):
        p1=n(r[0:x])
        #print "I", r[0:x], p1
        if p1==2:
            if n(r[x:])!=2:
                return 'NO'
            for y in range(x+1,len(r1)):
                p2=n(r[x:y])
                #print "J",r[x:y], p2
                if p2==3:
                    p3=n(r[y:])
                    #print "K",r[y:], p3
                    if p3==4:
                        return 'YES'
            
    return 'NO'

def m(s1,s2):
    if abs(s1)==1:
        return s2*s1
    if abs(s2)==1:
        return s1*s2
    if s1==s2:
        return -1
    if abs(s1)==abs(s2):
        return 1
    if abs(s1)+1==abs(s2) or (abs(s1)==4 and abs(s2)==2):
        sgn=1
    else:
        sgn=-1
    s=[2,3,4]
    s.remove(abs(s1))
    s.remove(abs(s2))
    return sgn*s[0]*int(math.copysign(1,s1*s2))

def n(s):
    s1=int(s[0])
    s=s[1:]
    while len(s)>0:
        s1=m(s1,int(s[0]))
        s=s[1:]
    return s1

raw_input("Got data?")
demo()
