__author__ = 'chang'
import math

def poli(x):
    x = str(x)
    l , r = 0 , len(x) - 1
    while x[l] == x[r] and l < r :
        l +=1
        r -=1
    if l >= r :
        return True
    return False

if __name__ == "__main__":

    t = int(raw_input())

    for cs in range(1,t+1):
        s = raw_input().split(' ')
        l = int(s[0])
        r = int(s[1])
        #print l , r

        ans = set()
        for i in range( int(math.floor(math.sqrt(l))) ,int(math.ceil( math.sqrt(r) )) + 1 ):
            if poli(i):
                x = i*i
                if x >= l and x <= r and poli(x):
                    ans.add(x)
                    #print x
        print "Case #%d: %d"%(cs ,len(ans) )
