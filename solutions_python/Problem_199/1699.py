
#1 is happy 0 is blank

def flip(i,s,f):#flip f pancakes in string s starting from index i
    s=[x for x in s]
    if i+f>len(s):
        print 'bad'
        return None

    for j in xrange(i,i+f):
        s[j]=(s[j]+1)%2

    return s
            



def allPossible(S,setS,f):#S is set of all orientations I know can be reached so far

    newPossible=[]
    newPS=set()
    for p in S:
        for i in xrange(len(p[0])-f+1):
            new=flip(i,p[0],f)
            strNew=str(new)
            #print strNew,new
            if not (strNew in setS) and not (strNew in newPS):
                newPS.add(strNew)
                newPossible.append((new,p[1]+1))

    setS=setS|newPS
    S=S+newPossible

    if len(newPossible)==0:
        return S

    return allPossible(S,setS,f)


def getAllWithOrder(l,f):
    S=[([1]*l,0)]
    setS=set()
    setS.add(str(S[0][0]))
    return allPossible(S,setS,f)

"""
allSolutions=[None,None]
for l in xrange(2,11):
    for f in xrange(2,l+1):
        ans=getAllWithOrder(l,f)
        allSolutions.append(ans)
"""

translate=dict()
translate['+']=1
translate['-']=0


f=open("prob1small.txt","r")
T=int(f.readline())

ans=[]
for line in f:
    l=line.split(' ')
    S=[translate[x] for x in l[0]]
    K=int(l[1])
    
    allPos=getAllWithOrder(len(S),K)
    flag=False
    for i in allPos:
        if i[0]==S:
            flag=True
            ans.append(i[1])
            
    if not flag:
        ans.append('IMPOSSIBLE')

f.close()

b=open("ans1small.txt","w")
for i in xrange(len(ans)):
    b.write("Case #"+str(i+1)+": "+str(ans[i])+"\n")


b.close()
