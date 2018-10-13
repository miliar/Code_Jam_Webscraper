import sys

searchString="welcome to code jam"
cache={}
cacheHits=0
cacheMisses=0

def optimizeString(test,searchString):
    test2="".join([x for x in test if x in searchString])
    while(test2 and searchString[-1]!=test2[-1]):
        test2=test2[:-1]
    print "Optimized len %d to len %d"%(len(test),len(test2))
    return test2

def outer_calculate(test,n,match):
    global cache,cacheHits,cacheMisses
    cache={}
    cacheHits=0
    cacheMisses=0
    return inner_calculate(test,n,match)
    
def inner_calculate(test,n,match):
    global cache,cacheHits,cacheMisses
    key=(n,len(match))
    c=cache.get(key,-1)
    if c==-1:
        c=0
        if not match:
            c=1
        else:
            x = match[0]
            test_len=len(test);
            while n<test_len:
                if test[n]==x:
                    c=c+inner_calculate(test,n+1,match[1:])
                n+=1
        cache[key]=c
        #print "added to cache %s=%d"%(repr(key),c)
        cacheMisses+=1
    else:
        #print "hit cache %s=%d"%(repr(key),c)
        cacheHits+=1
    return c

input=open("C-large.in","r")
dimension=input.readline().strip().split()
T=int(dimension[0])

output=open("C-large.out","w")

for i in range(1,T+1):
    print("\n\nCase %d of %d"%(i,T))
    line=input.readline().strip()
    line=optimizeString(line,searchString)
    n=outer_calculate(line,0,searchString)
    r=("0000"+str(n))[-4:]
    print "  %d => %s  ( cache hits/misses = %d/%d)"%(n,r,cacheHits,cacheMisses)
    output.write("Case #%d: %s\n"%(i,r))

input.close()
output.close()
print "finished"