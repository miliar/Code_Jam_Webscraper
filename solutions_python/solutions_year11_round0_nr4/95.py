import sys
import operator
cin = sys.stdin.readline

##derange = [0, 1]
##for i in xrange(2, 1003):
##    derange.append((i-1)*(derange[-1]+derange[-2]))

##def ncr(n, r):
##    pass
##
##
##answer = [0.0, 0.0]
##def soo(N):
##    

##for i in xrange(2,1040):
##    answer.push_back(soo(i))
    
    
    


def solve(actions):
    atime, btime = 0, 0
    mytime = 0
    aat, bat = 1, 1
    for who, where in actions:
        if who:
            #a goes
            extra_time = mytime - atime
            move_time = max(0, abs(where - aat) - extra_time)
            aat = where
            mytime = atime = mytime + move_time + 1            
        else:
            #b goes
            extra_time = mytime - btime
            move_time = max(0, abs(where - bat) - extra_time)
            bat = where
            mytime = btime = mytime + move_time + 1
    return mytime
                
        

if __name__ == '__main__':
    T = int(cin())
    for cnum in xrange(T):
        N = int(cin())
        arr = [int(i) for i in cin().strip().split()]
        print "Case #{0}: {1}".format(cnum+1, sum(1 for i in range(N) if arr[i] != i+1))
                    
            
        
    
