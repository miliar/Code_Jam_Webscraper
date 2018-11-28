import sys
filename='C-small-attempt5.in'
#filename='sample3'
f=open(filename,"r")
f2=open("result_"+filename,"w")
sys.stdout=f2
def cal(s) :
    sign=1
    if s[0].find('-')>=0 :
        sign^=1
        s[0]=s[0][1]
    if s[1].find('-')>=0 :
        sign^=1
        s[1]=s[1][1]
    rtn=''
    if s.count('i')==2 or s.count('j')==2 or s.count('k')==2  :
        rtn='1'
        sign^=1
    elif s.count('1')>=1 :
        if s[0]=='1' : rtn=s[1]
        elif s[1]=='1': rtn=s[2]
        else : rtn='1'
    elif s[0]=='i' and s[1]=='j' : rtn='k'
    elif s[0]=='j' and s[1]=='i' :
        rtn='k'
        sign^=1
    elif s[0]=='j' and s[1]=='k' : rtn='i'
    elif s[1]=='j' and s[0]=='k' :
        rtn='i'
        sign^=1
    elif s[0]=='k' and s[1]=='i' : rtn='j'
    elif s[1]=='k' and s[0]=='i' :
        rtn='j'
        sign^=1
    if sign :
        return rtn
    else :
        return '-'+rtn
    
    

t=f.readlines()
#print t

for i in xrange(1,int(t[0])+1) :
    d=t[2*i].strip()
    x,y=t[2*i-1].split()
    d=d*int(y)
    le=1
    #print d
    
    before=d[0]
    c=[]
    ans=False
    #i k -1
    while le<len(d) :
         #print before
         c.append(before)
         before=cal([before,d[le]])
         le+=1
    c.append(before)
    finder=c[:]
    finder.reverse()
    #print c
    try :
        finder.index('i')
        kpos=finder.index('k')
        kpos=len(c)-kpos-1
        pos1=finder.index('-1')
        pos1=len(c)-pos1-1
    except :
        print "Case #%d: No"%i
        continue
    #print c
    for j in xrange(len(c)) :
        if c[-1]!='-1' : break
        if c[j]=='i' and kpos>j :
            ans=True
        if ans : break;
         
    if ans :
        print "Case #%d: Yes"%i
    else :
        print "Case #%d: No"%i
f2.close()
