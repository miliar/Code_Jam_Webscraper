from sage.rings.integer import GCD_list

f = open('B-large.in', 'r')
fout = open('B-large.out', 'w')
C = int(f.readline().strip())
for c in range(C):
    line = f.readline().strip().split()
    N = int(line[0])
    ti = [int(line[i + 1]) for i in range(N)]
    ti.sort()
    diffs = [ti[i + 1] - ti[i] for i in range(N - 1)]
    #print diffs
    #w = GCD_list(diffs)
    #print w
    #print (-ti[0]) % w
    fout.write('Case #%d: ' % (c+1))
    fout.write(str((-ti[0]) % GCD_list(diffs)))
    fout.write('\n')
    
    
    
