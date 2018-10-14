f = open('A-large.in')
T = int(f.readline())
fout = open('out.txt', 'w')
"""
  N = 2, K = 3
  00
  10
  01
  11
"""

def is_on(N, K):
  return K % (2**N) == 2**N - 1;

for i in range(1, T + 1):
  N, K = [int(j) for j in f.readline().split()]
  
  fout.write('Case #%d: %s\n' % (i, ('ON' if is_on(N, K) else 'OFF')))

fout.close()  
f.close()