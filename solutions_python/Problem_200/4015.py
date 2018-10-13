tidyList=[]
num=[]

def checkTidy(n):
    #try:
        #return tidyList[n]
    #except:        
    tidy=0
    del num[:]
    i=0
    while n:
        num.insert(i, n%10)
        n/=10
        i+=1
    lastP=-1
    #print num[::-1]
    i=0
    for p in num[::-1]:
        i+=1
        if lastP==-1:
            lastP=p
            continue
        else:
            if lastP>p:
                tidy=i                
                break
            else:
                lastP=p
                
    #print tidy
    #tidyList.insert(n, tidy)            
    return tidy

t=int(raw_input())
x=1
nines=9999999999999999999999

while(t):
    now = int(raw_input())
    isTidy = checkTidy(now)
    while isTidy != 0:
        temp = now % 10**((len(num)-isTidy)+1)
        nins = nines % 10**((len(num)-isTidy)+1)
        #print temp
        now-=10**((len(num)-isTidy)+1)
        now-=temp
        now+=nins
        isTidy=checkTidy(now)
    
    print "Case #%d:" % x,
    print now
    x+=1
    t-=1
