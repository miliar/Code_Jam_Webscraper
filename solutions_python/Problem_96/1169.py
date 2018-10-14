'''
Created on 14/apr/2012

@author: matteo
'''


countsurp = 0
countwin = 0

def calc(p,score):
    if score >= p:
        n = int(score/3)
        trip = [n,n,n]
        while sum(trip) != score:
            for i in xrange(len(trip)):
                if sum(trip) < score:
                    trip[i] += 1
                elif sum(trip) > score:
                    trip[i] -= 1
                if sum(trip) == score:
                    break    
        trip = sorted(trip)
        return evaluate(trip,p,2)
    
    else:
        return 0, 0
    

def evaluate(trip,p,chpos):
    if max(trip)>=p:
        return 1, 0
    else:
        trip[chpos] += 1
        trip[chpos-1] -= 1
        if trip[chpos] <= 10 and trip[chpos-1] >= 0:
            if max(trip) >= p: 
                if abs(trip[chpos]-trip[chpos-1])<=2:
                    return 1, 1
                else:
                    chpos -= 1
                    if chpos > 1:
                        return evaluate(trip,p,chpos) 
        else:
            trip[chpos] -= 1
            trip[chpos-1] += 1 
            chpos -= 1
            if chpos > 1:
                return evaluate(trip,p,chpos) 
            

        return 0, 0
             
def test(ifp):
    nrows = int(ifp.readline())
    ofp = open("../dancing/out2.txt" ,"w")
    for i in xrange(1,nrows+1):
        line = (ifp.readline().strip())
        sline = line.split(' ')
        N = int(sline[0])
        S = int(sline[1])
        p = int(sline[2])
        countwin = 0
        for player in xrange(3,N+3): 
            win, surp = calc(p, int(sline[player]))
            if surp == 0:
                countwin += win
            else:
                S = S - surp
                if S >= 0:                   
                    countwin += win


        msg = "Case #%d: %d" % (i,countwin)
        print msg
        ofp.write(msg + '\n')
    ofp.close() 

if __name__ == "__main__":
#    print calc(5,11)
    ifilename = '../dancing/B-large.in' 
#    ifilename = '../dancing/test.in' 
    if ifilename != "":
        print ifilename
        ifp = open(ifilename, "r")        
        test(ifp)      
        ifp.close()
