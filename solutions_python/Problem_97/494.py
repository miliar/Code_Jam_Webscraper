import time


def process(filein):

    f_in=open(filein+".txt").read().split('\n')
    f_out=open(filein+"_out.txt",'w')

    n=int(f_in[0])

    for i in range(n):
        t=f_in[1+i]


        low,high=t.split(' ')
        ans=solve2(int(low),int(high))

        f_out.write("Case #%d: %s\n" % (1+i,ans))
    f_out.close()



def solve2(low,high):
    ans=0
    for n in range(low,high+1):
        ans+=len(set([p for p in cache[n] if low<=n<p<=high]))
    return ans
    
def cycles(n):
    s=str(n)
    poss=[int(s[i:]+s[:i]) for i in range(1,len(s)) if s[i]!='0']
    return [p for p in poss if n<p]


cache={}
def precalc():
    for i in range(1,2000000):
        cache[i]=cycles(i)

start=time.time()
print time.time()-start
precalc()
print time.time()-start
process("2large")
print time.time()-start

    
