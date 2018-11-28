__author__ = 'franyell'




def getNeg(c):
    if len(c)<2:
        c='-'+c
    else:
        c=c[1:]
    return c

def getTimes(c,n):

    iv={ 'i':'-1','j':'k', 'k':'-j'}
    jv={ 'i':'-k','j':'-1','k':'i'}
    kv={ 'i':'j', 'j':'-i','k':'-1' }
    r=''
    if c=='1':
        return n
    if n=='1':
        return c

    if c=='-1':
        return getNeg(n)
    if n=='-1':
        return getNeg(c)

    sig1=1
    sig2=1
    if len(c)>1:
        sig1=-1
        c=c[1:]
    if len(n)>1:
        sig2=-1
        n=n[1:]

    r=None
    if c=='j':
        r=jv[n]
    elif c=='k':
        r=kv[n]
    elif c=='i':
        r=iv[n]

    if sig1==sig2:
        return r
    else:
        return getNeg(r)


def mymain():

    infile= open("in.txt")
    outfile=open("out.txt","w")
    cases = int(infile.readline().strip("\n"))+1

    for case in range(1,cases):
        print("case #" +str(case))
        t=infile.readline().strip('\n').split()
        s=infile.readline().strip('\n')
        x=reduce(s,t)
        createOutput(outfile,case,x)


    infile.close()
    outfile.close()

def createOutput(out,case,min):
    out.write("Case #"+str(case)+": "+str(min)+"\n")

def noMore(s1):
     y=len(s1)
     if s1[0]=='-' and y<=2:
             return True
     if y<=1:
             return True
     return False

def reduce(s,t):
    r='NO'
    size=int(t[0])
    mult=int(t[1])

    if size==1:
        return "NO"
    if mult==1 and size == 3:
        if s=="ijk":
            return "YES"
        return "NO"

    if mult==1 and size<3:
        return "NO"

    str1=['i','j','k']
    count=0

    s1=""
    notDone=True
    while(notDone):
        # print(' top while: '+str(len(s1))+" mult: "+str(mult))
         if mult>0:
            s1=s1+s
         y=len(s1)
         if s1[0]=='-' and y<=2:
             return "NO"
         if y<=1:
             return "NO"
         r=minimize(s1,str1[count])
        # print(r)
         if count==0:
             #Looking i
             if r[0]==True:
                 count+=1
                 s1=r[2]
             else:
                s1=r[1]

         elif count==1:
             #looking j
            if r[0]==True:
                 count+=1
                 s1=r[2]
            else:
                s1=r[1]
         elif count==2:
             if r[0]==True:
                 s1=r[2]
                 if len(s1)==0 and mult<=1:
                     return "YES"
                 elif mult<=1  and noMore(s1):
                     return "NO"
                 s1=r[1]+s1

             else:

                s1=r[1]
         mult-=1
    return "NO"



def minimize(s,c1):
    s1=''

    l=len(s)
   # print(l)
    x=1
    actual=s[0]
    if s[0]=='-':
        actual=s[0:2]
        x+=1


    found=False
    #print("\n\n"+s+" "+c1)
    while(x<(l)):
        c=""
        if s[x]=='-':
            #print('what the fuck')
            c=s[x:x+2]
            #print(c)
        else:
             c=s[x]
        #print(str(actual)+ "*"+ str(c),end="")
        actual=getTimes(actual,c)
       # print('= '+actual)

        if actual==c1:
           # print("found "+str(x)+" "+c)
            found=True
            x+=1
            break
        x+=1
    if found:

        return [found,actual,s[x:]]
    else:
        return [False,actual,[]]




mymain()