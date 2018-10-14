import sys
import fractions

infile = sys.stdin

def find_note(notes, L, H):
    for x in xrange(L,H+1):
        good = True
        for n in notes:
            if x==n or (x>n and x%n==0) or (n>x and n%x==0):
                pass
            else:
                good = False
                break
        if good: return x
    return None
    

T = int(infile.readline())
for i in xrange(T):
    N,L,H = map(int, infile.readline().split())
    notes = map(int, infile.readline().split())
    result = find_note(notes, L, H)
    print("Case #%d: %s" % (i+1, result if result else "NO"))
