
def doProb(fname, ofname):
    #do problem B given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    T = int(f.readline());

    output = ['Case #' + str(i) + ': '+ doStuff(map(int, f.readline().split())) + '\n' for i in xrange(1,T+1)]
    f.close();      

    of.writelines(output);
    of.close();

def doStuff(Line):    
    [L,t,N,C] = Line[:4]    
    A = Line[4:]
    stars = [A[i%C] for i in xrange(N)]
    
    #Brute Force for the small dataset
    
    if(L==0):
        #compute time
        return str(computeTime(stars, [], t))
    elif(L==1 or N==1):
        #choose where to put the booster
        rTot = runningTotal(stars)
        bestTime = rTot[-1]        
        for i in xrange(N):
            x = addBoost1(rTot, stars, t, i)            
            if(x<bestTime):
                bestTime = x
        return str(bestTime)
    elif(L==2):
        #choose where to put the two boosters
        rTot = runningTotal(stars)
        bestTime = rTot[-1]        
        for i in xrange(N-1):
            for j in xrange(i+1,N):                
                x = addBoost2(rTot, stars, t, i, j)                
                if(x<bestTime):
                    bestTime = x                    
        return str(bestTime)
    print 'next time'

def runningTotal(stars):
    total = [0 for i in stars]
    total[0] = 2*stars[0]
    for i in xrange(1,len(stars)):
        total[i] = total[i-1] + 2*stars[i]
    return total

def addBoost1(rTot, stars, t, i):
    if(i==0):
        cur = 0
    else:
        cur = rTot[i-1]
    
    if(t>cur+2*stars[i]):
        return rTot[-1]
    elif(t<cur):
        return rTot[-1] - stars[i]
    else:
        ttb = float(t-cur)
        dtb = ttb/2
        drem = float(stars[i])-dtb
        return int(rTot[-1]-2*stars[i]+drem+ttb)

def addBoost2(rTot, stars, t, i, j):
    if(i==0):
        cur = 0
    else:
        cur = rTot[i-1]

    diff = 0
    if(t>cur+2*stars[i]):
        diff = 0
        cur2 = rTot[j-1]
    elif(t<cur):
        diff = stars[i]
        cur2 = rTot[j-1]-diff
    else:
        ttb = float(t-cur)
        dtb = ttb/2
        drem = float(stars[i])-dtb
        diff =  int(2*stars[i]-drem-ttb)
        cur2 = rTot[j-1]-diff

    if(t>cur2+2*stars[j]):
        return rTot[-1]-diff
    elif(t<cur2):
        return rTot[-1]-stars[j]-diff
    else:
        ttb = float(t-cur2)
        dtb = ttb/2
        drem = float(stars[j])-dtb
        return int(rTot[-1]-diff-2*stars[j]+drem+ttb)
        
           
def computeTime(stars, boost, t):
    total = 0    
    for i in xrange(len(stars)):
        if(i in boost):
            if(t<total):
                #full boost
                total += float(stars[i])
            elif(t>total+2*stars[i]):
                #no boost
                total += 2*float(stars[i])
            else:
                #partial boost
                ttb = float(t-total)                
                dtb = ttb/2                
                drem = float(stars[i])-dtb
                total += (drem + ttb)
        else:
            total += 2*float(stars[i])    
    
    return int(total)
            
                
            
            

pf = 'C:\\Python27\\gcj11\\Round1C\\B';
doProb(pf + '\\bsmall.in', pf + '\\bsmall.out')
#doProb(pf + '\\blarge.in', pf + '\\blarge.out')
#doProb(pf + '\\b.in', pf + '\\b.out')

