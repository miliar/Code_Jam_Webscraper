import time


def process(filein):

    f_in=open(filein+".txt").read().split('\n')
    f_out=open(filein+"_out.txt",'w')

    n=int(f_in[0])

    for i in range(n):
        t=f_in[1+i]


        parts=map(int,t.split(' '))
        ans=solve3(parts[0],parts[1],parts[2],parts[3:])

        f_out.write("Case #%d: %s\n" % (1+i,ans))
    f_out.close()


def solve3(N,S,p,t):
    count={(True,True):0,
           (False,True):0,
           (True,False):0,
           (False,False):0}
    for i in range(N):
        u=unsurprising(t[i])
        s=surprising(t[i])
        nu=(u!=[] and max(max(u))>=p)
        ns=(s!=[] and max(max(s))>=p)
        count[nu,ns]+=1
    
    score=count[(True,True)]+min(S,count[(False,True)])+count[(True,False)]
    return score

    
def allways(score):

    def ways(score,n):
        if n==1:
            if 0<=score<=10:
                return [[score]]
            else:
                return []
        else:
            return [[i]+w for i in range(0,11)
                          for w in ways(score-i,n-1)
                          if i<=w[0]]

    return ways(score,3)

def unsurprising(score):
    return [(a,b,c) for (a,b,c) in allways(score)
                    if c-a<=1]

def surprising(score):
    return [(a,b,c) for (a,b,c) in allways(score)
                    if c-a==2]

process("4large")
