f = file(r'A-large.in', 'rt')
out = file(r'A-large.out', 'w+t')
t=int(f.readline())

for i in xrange(t):
    (n, k) = map(int, (f.readline().split()))
    state = "OFF"
    if ((k+1)%(2**n) == 0):
        state = "ON"
    out.write('Case #%d: %s\n' % (i+1, state))
f.close()
out.close()
print 'Done!'