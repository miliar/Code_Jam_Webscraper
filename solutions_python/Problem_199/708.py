# Code Jam 2017 Qualification round
# MichelJ
# Problem A: Oversized Pancake Flipper

def solve_greedy(s, k):
    l = len(s)
    st = [c == "+" for c in s]
    def flip(i):
        for j in xrange(i, i + k):
            st[j] = not st[j]
    try:
        nflips = 0
        for i in xrange(l):
#            print st
            if not st[i]:
                flip(i)
                nflips += 1
        return nflips
    except:
        return -1

tc = [("---+-++-", 3), ("+++++", 4), ("-+-+-", 4)]
def test():
    for t in xrange(len(tc)):
        s, k = tc[t]
        res = solve_greedy(s, k)
        print "Case #%d:"%(t + 1), res if res >= 0 else "IMPOSSIBLE"

def main():
    for t in xrange(input()):
        s, k = raw_input().split()
        k = int(k)
        res = solve_greedy(s, k)
        print "Case #%d:"%(t + 1), res if res >= 0 else "IMPOSSIBLE"
        
main()
