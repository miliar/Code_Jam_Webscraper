#import psyco
#psyco.jit() 
#from psyco.classes import *
#psyco.full()

infile= open('a')
outfile = open('b', 'w')

def scoreToTupList(score):
    a, b, c, l = 0, 0, score, []
    while a<=10:
        b = 0
        c = score
        score -= 1
        while b<=10:
            if c<0: break
            if c<=10:
                if abs(a-b)<3 and abs(b-c)<3 and abs(c-a)<3:
                    l.append((a, b, c))
            c -= 1
            b += 1
        a += 1    
    return l
 
def isSurprising((a, b, c)):
    if  abs(a-b)==2 or abs(b-c)==2 or abs(c-a)==2:
        return True
    else:
        return False

def isGood((a, b, c), p):
    if((a>=p) or (b>=p) or (c>=p)):
        return True
    else:
        return False        

def sumR((a1, b1), (a2, b2)):
    return (0, b1+b2)

counter = 0
T, marked = int(infile.readline()), []
for line in infile:
    l, lineFinal = line.split(), []
    N, S, P = int(line.split()[0]), int(line.split()[1]), int(line.split()[2])
    gListTuples = map(scoreToTupList, map(int, l[3:]))
    for i in xrange(len(l[3:])):
        tl = gListTuples[i]
        if len(tl) == 0: continue
        s, ns = 0, 0
        for j in xrange(len(tl)):   #going through all the tuples
            if isSurprising(tl[j]):
                if s==0:
                    s = 2
                if isGood(tl[j], P):
                    s = 1
            else:
                if isGood(tl[j], P):
                    ns = 1    
        lineFinal.append((s, ns))
    
    l0, l1, l2 = [], [], []
    for i in xrange(len(lineFinal)):
        s, ns = lineFinal[i]
        if s == 0:
            l0.append(lineFinal[i])
        elif s==1:
            l1.append(lineFinal[i])
        else:
            l2.append(lineFinal[i])
    if(len(l0)==0): sr0 = 0
    else:    (h, sr0) = reduce(sumR, l0)
    if(len(l1)==0): sr1 = 0
    else:    (h, sr1) = reduce(sumR, l1)
    if(len(l2)==0): sr2 = 0
    else:    (h, sr2) = reduce(sumR, l2)
  
    if S <= len(l1): #no need to look into l2
        if sr1 > len(l1)-S: temp=len(l1)-S
        else:   temp=sr1
        ans = sr0 + S + temp + sr2
    else:
        if sr2 > len(l2)-(S-len(l1)): temp=len(l2)-(S-len(l1))
        else:   temp=sr2
        ans = sr0 + len(l1) + temp
    outfile.write("Case #"+str(counter+1)+": "+str(ans)+"\n")
    counter += 1

print "KODEROK"
