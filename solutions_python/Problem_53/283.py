f = open('A-large.in', 'r')
fout = open('out.out', 'w')
T = int(f.readline().strip())
for i in range(T):
    line = f.readline().strip().split()
    N = int(line[0])
    K = int(line[1])
    fout.write('Case #%d: ' % (i+1))
    fout.write('ON' if K % (2**N) == (2**N - 1) else 'OFF')
    fout.write('\n')
    
    
    
