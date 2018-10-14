if __name__ == '__main__':
  #f = open('Downloads/A-small-attempt1.in')
  f = open('Downloads/A-large.in')
  #f = open('test.txt')
  n = int(f.readline())
  for i in range(1,n+1):
    l = f.readline()
    n, k = l.strip().split()
    n, k = int(n), int(k)
    snapper = bin(k)[2:]
    status = 'ON'
    if len(snapper) < n:
      status = 'OFF'
    else:
      for d in snapper[-n:]:
        if d == '0':
          status = 'OFF'
    print 'Case #%d: %s'%(i,status)
     
