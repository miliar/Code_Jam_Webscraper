for case in xrange(input()):
   r, k, n = [int(s) for s in raw_input().split()]
   g = [int(s) for s in raw_input().split()]
   cash = 0
   for i in xrange(r):
      load = []
      while g and sum(load) + g[0] <= k:
         load.append(g[0])
         del g[0]
      cash = cash + sum(load)
      g.extend(load)
   print 'Case #%d: %d' % (case+1, cash)
