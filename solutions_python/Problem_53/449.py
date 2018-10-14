
f = open('A.in')
lines = f.read().splitlines()
f.close()

T = int(lines.pop(0))
results = []
for k in xrange(T):
    N, count = [int(x) for x in lines.pop(0).split()]
    
    answer = 'ON' if (count+1)%(2**N) == 0 else 'OFF'
    results.append('Case #%d: %s' % (k+1,answer))

f = open('A.out','w')
f.write('\n'.join(results)+'\n')
f.close()

#print '\n'.join(results)+'\n'
