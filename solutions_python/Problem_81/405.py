import sys


#####################

def printMove():
    N = input()
    scores=[]
    for i in xrange(N):
        scores.append(raw_input())
        
    #print scores
    OWP=[]
    
    for i in xrange(N):
        xscores=scores[:]
        rec=[]
        for k in xrange(N):
            if scores[i][k] is "0" or scores[i][k] is "1":
                rec.append(k)
        tempOWP=0
        for r in rec:
            count = 0
            temp=0
            for t in xrange(N):
                if t is i:
                    continue
                if scores[r][t] is "1" or scores[r][t] is "0":
                    count = count + 1
                if scores[r][t] is "1":
                    temp = temp + 1
            temp = float(temp)/count
            tempOWP = tempOWP + temp
        #print temp,len(rec)
        tempOWP = float(tempOWP)/len(rec)
        OWP.append(tempOWP)
    #print OWP
        

            
    for i in xrange(N):
        WP = float(scores[i].count("1"))/(scores[i].count("1")+scores[i].count("0"))
        nOWP = OWP[i]
        nOOWP = 0
        count = 0
        for t in xrange(N):
            if t is i:
                continue
            if scores[i][t] is "1" or scores[i][t] is "0":
                count = count + 1
                nOOWP = nOOWP + OWP[t]
                #print OWP[t]
      
        nOOWP = float(nOOWP)/count
        
        RPI = (0.25 * WP) + (0.50 * nOWP) + (0.25 * nOOWP)
        print RPI
                
    return 1

####################
sys.stdin = open("in.txt", "r")

sys.stdout = open("out.txt", "w")
no = input()
for i in xrange(0,no):
    print "Case #{0}:".format(i+1)
    printMove()

sys.stdout.close()
