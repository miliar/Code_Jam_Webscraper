import sys
import re

fin = open(sys.argv[1], 'r')
fout = open(re.sub(r'\.\w+$', '.out', sys.argv[1]), 'w')

def out(case, s):
    output = 'Case #' + str(case+1) + ': ' + str(s)
    fout.write(output + '\n')
    print output
    
def mapint(s):
    return map(int, s.split(' '))

for T in xrange(int(fin.readline())):
    A, B, K = mapint(fin.readline())
    cnt=0
    for a in xrange(A):
      for b in xrange(B):
        if a&b < K:
          cnt += 1
    out(T, cnt)

fout.close()
