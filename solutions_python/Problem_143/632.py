fname = 'B-small-attempt0'
fin = open('%s.in' % fname,'r')
fout = open('%s.out' % fname,'w')

T = int(fin.readline())

for i in range(T):
  [A,B,K] = [int(x) for x in fin.readline().split(' ')]
  print [A,B,K]
  
  nwinners = 0
  for x1 in range(A):
    for x2 in range(B):
      if x1 & x2 < K:
        nwinners += 1
  
  fout.write('Case #%u: %0.9g\n' % (i+1,nwinners))

fin.close()
fout.close()