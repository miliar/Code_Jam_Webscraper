maxSize = 1000000
def backtrack(mote,m,count,A):
    if m == len(mote) or A > maxSize:
        return count
    elif mote[m] < A:
        return backtrack(mote,m+1,count,A+mote[m])
    else:
        if A > 1:
            return min(backtrack(mote,m+1,count+1,A),backtrack(mote,m,count+1,2*A-1))
        else:
            return backtrack(mote,m+1,count+1,A)

def solve():
    T = int(raw_input())
    for t in xrange(T):
        A,N = map(int,raw_input().split(" "))
        mote = list(map(int,raw_input().split(" ")))
        mote.sort()
        res = backtrack(mote,0,0,A)
        print "Case #" + str(t+1) + ":",res

solve()
