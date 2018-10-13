import sys

cin = sys.stdin.readline


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
        lin = cin().strip().split()
        N = lin[0]
        actions = []
        for i in xrange(1, len(lin), 2):
            actions.append((lin[i] == 'O', int(lin[i+1])))

        print "Case #{0}: {1}".format(cnum+1, solve(actions))
                    
            
        
    
