import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    Smax, S = f.readline().split()
    
    standing = 0
    invites = 0

    for l, c in enumerate(S):
        if standing + invites < l:
            invites += (l - standing - invites)
        standing += int(c)
    
    print 'Case #%i:' % (t + 1), invites
