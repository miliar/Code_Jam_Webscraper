import psyco
psyco.full()

def main():
    def check(b):
        red=0
        blue=0
       # for q in xrange(0,N):
       #     print b[q], "\n"
       # print "\n"
        for k in xrange(0, N):
            for q in xrange(0,N):
                if b[k][q]=='.':
                    b[k].pop(q)
                    b[k].insert(0,'.')
       # for q in xrange(0,N):
       #     print b[q], "\n"
        for k in xrange(0,N):
            for j in xrange(0,N-K+1):
                if b[j][k]=="." or (b[j][k]=="R" and red==1) or (b[j][k]=="B" and blue==1):
                    continue
                if test(map(lambda a: b[j+a][k], xrange(0,K))):
                    if b[j][k]=="R":
                        red=1
                    if b[j][k]=="B":
                        blue=1
        for k in xrange(0,N-K+1):
            for j in xrange(0,N-K+1):
                if b[j][k]=="." or (b[j][k]=="R" and red==1) or (b[j][k]=="B" and blue==1):
                    continue
                    
                if test(map(lambda a: b[j+a][k+a], xrange(0,K))):
                    if b[j][k]=="R":
                        red=1
                    if b[j][k]=="B":
                        blue=1
        
        for j in xrange(K-1,N):
            for k in xrange(N-K+1):
                if b[j][k]=="." or (b[j][k]=="R" and red==1) or (b[j][k]=="B" and blue==1):
                    continue
                    
                if test(map(lambda a: b[j-a][k+a], xrange(0,K))):
                    if b[j][k]=="R":
                        red=1
                    if b[j][k]=="B":
                        blue=1
        
        for j in xrange(N):
            for k in xrange(N-K+1):
                if b[j][k]=="." or (b[j][k]=="R" and red==1) or (b[j][k]=="B" and blue==1):
                    continue
                    
                if test(b[j][k:k+K]):
                    if b[j][k]=="R":
                        red=1
                    if b[j][k]=="B":
                        blue=1
                         
        if red==0 and blue==0:
            return "Neither"
        if red==1 and blue==0:
            return "Red"
        if red==0 and blue==1:
            return "Blue"
        if red==1 and blue==1:
            return "Both"
                
                    
    def test(vals):
        if vals:
            i = iter(vals)
            first = i.next()
            for item in i:
                if first != item:
                    return False
        return True
    
    cases = int(raw_input())
    for i in xrange(0, cases):
        N, K = map(int, raw_input().split(" "))
       # print N,K
        board=[]
        for j in xrange(0, N):
            board.append(list(raw_input()))
            
        print "Case #%i: %s" % (i+1, check(board))
        
    
           
main()