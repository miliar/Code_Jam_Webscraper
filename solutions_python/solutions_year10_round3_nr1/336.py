def crosswired(AB):
   res = 0
   for i1 in xrange(len(AB)):
      for i2 in xrange(i1+1, len(AB)):
         if (AB[i1][0] < AB[i2][0] and \
             AB[i1][1] > AB[i2][1]) or \
            (AB[i1][0] > AB[i2][0] and \
             AB[i1][1] < AB[i2][0]):
            res += 1
   return res

data = open('A-small-attempt0.in', 'r').read().split('\n')

T = int(data.pop(0))

for t in range(T):
   N = int(data.pop(0))
   AB = []
   for n in range(N):
      AB.append( map(int, data.pop(0).split()) )
   print 'Case #' + str(t+1) + ': ' + str(crosswired(AB))
