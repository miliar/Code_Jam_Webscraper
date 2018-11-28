def evaluate (n,k):
    return k % (2**n) == 2**n-1
    
f = open('small.txt')
size = int(f.readline())

inputs = []
for i in range(size):
  n,k = map(int,f.readline().split())
  inputs += [(n,k)]
  
for i,(n,k) in enumerate(inputs):
  print 'Case #%i: %s' % (i+1, ['OFF','ON'][evaluate(n,k)])