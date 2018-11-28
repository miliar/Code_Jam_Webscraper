import sys

def next(s,closing=None,add=0):
    s=s.lstrip(" ")
    if closing:
        if len(closing)==2:
            i=s.find(closing[0])
            j=s.find(closing[1])
            if i==-1: i=j
            if j!=-1: i=min(i,j)
        else:
            i=s.find(closing)
    else:
        i=s.find(" ")
        j=s.find(")")
        k=s.find("(")
        if i==-1: i=max(j,k)
        if j!=-1: i=min(i,j)
        if k!=-1: i=min(i,k)
    if i<0:i=len(s)
    if i==0:
        r=s[0]
        s=s[1:]
        return (r,s)
    r=s[0:i].rstrip(" ")
    s=s[i+1+add:]
    return (r,s) 


f=open("A-small.in")
o=open("A-small.out","w")
lines=f.readlines()
for i,line in enumerate(lines):
    lines[i]=line.rstrip("\n")
N=int(lines[0])
followingline=1
for n in range(0,N):
    #print "beginning",n
    o.write("Case #"+str(n+1)+":\n")
    L=int(lines[followingline])
    followingline+=1
    tree=" ".join(lines[followingline:followingline+L])
    followingline+=L
    #print "tree",tree
    A=int(lines[followingline])
    followingline+=1
    animals=lines[followingline:followingline+A]
    followingline+=A
    for animal in animals:
        token=tree[:]
        animobj=animal.split(" ")
        desc=animobj[2:]
        #print "entering animal",animobj[0]
        p=1.
        openbraces=0
        while (True):
            token=token.lstrip(" ")
            if token[0]==")":
                #print "-"
                token=token[1:]
                openbraces-=1
                if openbraces==0:
                    #print "result",p
                    o.write("%.7f\n"%(p))
                    break
                continue
            if token[0]=="(":
                token=token[1:]
                openbraces+=1
                #print "+"
            ntoken,token=next(token,"()",-1)
            while ntoken=="":
                #print "N%s:T:%s" %(ntoken, token)
                ntoken,token=next(token,"()",-1)
            #print "processing",ntoken
            weight,descs=next(ntoken," ")
            p*=float(weight)
            #print "now",p
            #print "left",token
            #print "checking ",descs
            for desc1 in descs,:
                if desc1=="":continue
                if desc1 not in desc:
                    #print "cotinuing",desc1,"not in",desc
                    shouldbeopen=openbraces
                    #print shouldbeopen
                    for i,ch in enumerate(token):
                        if ch=="(":
                            openbraces+=1
                        if ch==")":
                            openbraces-=1
                            if openbraces==shouldbeopen:
                                if openbraces==0:
                                    #print "result",p
                                    o.write("%.7f\n"%(p))
                                    break
                                token=token[i+1:]
                                #print token
                                break
            if not descs:
                #print "result",p
                o.write("%.7f\n"%(p))
                break

o.close() 
