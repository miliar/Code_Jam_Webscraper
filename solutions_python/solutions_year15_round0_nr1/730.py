
import sys

fin = sys.stdin
fout = sys.stdout

T = int(fin.readline())
for t in range(T):
    S = map(int, fin.readline().strip().split()[1])
    
    standing = 0
    added = 0
    for required, numpeople in enumerate(S):
        if required>standing:
            added += required-standing
            standing = required
        standing += numpeople
    fout.write("Case #%i: %i\n" % (t+1, added))
       
