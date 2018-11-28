from sys import stdin

def process():
    stdin.readline() #omit the input len
    for lno, line in enumerate(stdin):
        ints = [int(i) for i in line.split()]
        N,S,p,T = ints[0],ints[1],ints[2],ints[3:]
        countp = 0
        for t in T:
            if p > t: continue
            if t / 3 >= p :
                countp += 1
            elif t / 3 == p - 1:
                if t % 3 > 0:
                    countp += 1
                else:
                    if S > 0:
                        countp += 1
                        S -= 1
            elif t / 3 == p - 2 and t % 3 == 2:
                if S > 0:    
                    countp += 1
                    S -= 1
        print "Case #%d: %d"% (lno+1,countp)
        
if __name__=="__main__":
    process()
