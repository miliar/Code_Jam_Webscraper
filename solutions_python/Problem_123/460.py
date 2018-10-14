import sys

def absorb(A, motes):
    while len(motes) > 0 and A > motes[0]:
        A += motes[0]
        del motes[0]
    return A


def dfs(A, motes):
    if not motes or A == 1:
        return len(motes)
    add_motes = 0
    motes_len = len(motes)
    while A <= motes[0]:
        A += A-1
        add_motes += 1
    A = absorb(A, motes)
    return min(motes_len, add_motes + dfs(A, motes))




if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        A, N = [ int(e) for e in sys.stdin.readline().strip().split()]
        motes = [ int(e) for e in sys.stdin.readline().strip().split()]
        motes.sort()
        #print A, motes
        A = absorb(A, motes)
        #        print A, motes
        print "Case #%d: %d" % (t+1, dfs(A, motes))
