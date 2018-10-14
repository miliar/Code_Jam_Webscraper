import string

def isPalindrome(strg):
    sz = len(strg)
    if sz == 1:
        return True
    elif sz == 2:
        return strg[0] == strg[1]
    else:
        if strg[0] != strg[-1]:
            return False
        else:
            return isPalindrome(strg[1:-1])

def getStartPoint(a,b):
    rt = a**0.5
    if rt == int(rt): return a
    else: return (int(rt)+1)**2

def numFairAndSquare(ab):
    sab = ab.split(' ')
    a = int(sab[0])
    b = int(sab[1])
    if b < 100000:
        if a == 1 and b == 1:
            return 1
        else:
            st = getStartPoint(a,b)
            ct = 0
            nxt = st
            
            while nxt <= b:
                if isPalindrome(str(nxt)) and isPalindrome(str(int(nxt**0.5))):
                    ct += 1
                nxt = int((nxt**0.5 + 1)**2)
            return ct
    else:
        allRange = splitter(sab[0],sab[1])
        ct1 = 0
        for a,b in allRange:
            st = getStartPoint(a,b)
            ct = 0
            nxt = st
            if (b % 10) == 0 and a > 9:
                notMore = b/2
            else:
                notMore = b
            siz = len(str(a))
            sp1 = 15*(10**(siz-2))
            
            sp2 = 4*(10**(siz-1)) + 8*(10**((siz-1)/2)) + 4
    
            ck = 0
            while nxt < notMore :
                if isPalindrome(str(nxt)) and isPalindrome(str(int(nxt**0.5))):
                    ct += 1
    
                nxt = int((nxt**0.5 + 1)**2)
                                       
                if siz >= 3 and nxt >= sp1 and ck == 0:
                    ck = 1
                    nxt = sp2
            ct1 += ct
        return ct1
                                       
                                   
                
            
            
            
                                           
            

def splitter(sa,sb):
    hld = []
    b = int(sb)
    a = sa
    sz = len(a)
    sz2 = len(sb)
    st = int(a)
    if (sz % 2 ) == 1:
        en = 10**sz
        if en>b:
            en = b
            hld.append((st,en))
            return hld
        hld.append((st,en))
        st = 10**(sz-1)
    else:
        st = 10**sz
        en = 10**(sz+1)
        if st >= b: return hld
        hld.append((st,en))
        if en >= b: return hld
        
    r1 = len(str(st))
    r2 = sz2
    st = st*100
    en = en*100
    while st <= b:
        if en > b:
            en = b
            hld.append((st,en))
            return  hld
        hld.append((st,en))
        st = st*100
        en = en*100
    return hld
            

    
    

      
        
    
inFile = open('C-small-attempt0.in','r')
outPut = open('fairAndSquare1.in','w')
inPut = inFile.read()
inPut = inPut.split('\n')
T = int(inPut[0])

Cases = inPut[1:]
emt = Cases.count('')
for h in range(emt):
    Cases.remove('')
    
for k in range(1,T+1):
    outPt = numFairAndSquare(Cases[k-1])
    outPut.write('Case #%d:' % (k) + " "+str(outPt)+'\n')
        
inFile.close()
outPut.close()
