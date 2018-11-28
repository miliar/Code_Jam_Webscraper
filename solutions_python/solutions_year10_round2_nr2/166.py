for case in xrange(input()):
   n, k, b, t = [int(s) for s in raw_input().split()]
   xi = [int(s) for s in raw_input().split()]
   vi = [int(s) for s in raw_input().split()]
   ti = [(b-xi[i] + vi[i] - 1) / vi[i] for i in xrange(n)]
   output = 'IMPOSSIBLE'
   if len([x for x in ti if x <= t]) >= k:
      ti.reverse()
      swaps, chicks = 0, 0
      for i, x in enumerate(ti):
         if x <= t:
            swaps += len([p for p in ti[:i] if p > t])
#            queue = len([p for p in ti[:i] if p > k])
#            swaps += queue - reversed(vi)
            chicks += 1
            if chicks == k:
               break
      output = str(swaps)
   print 'Case #%d: %s' % (case+1, output)
