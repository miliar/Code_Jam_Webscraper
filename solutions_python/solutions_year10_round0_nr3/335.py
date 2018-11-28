import sys

input = open(sys.argv[1])
n = int(input.readline())

for nCase in xrange(1, n+1):
  R,k,N = map(lambda x: int(x), input.readline().strip().split(' ') )
  g = map(lambda x: int(x), input.readline().strip().split(' ') )

  memo = [(-1, -1) for i in g]

  euro = 0
  gi = 0
  max = len(g)

  one_loop_index = []
  for i in xrange(1, R+1):
    #print memo

    if memo[gi][0] == -1:
      gi_sum = 0
      for j in xrange(gi, gi + max):
        gi_current = j % max

        if gi_sum + g[gi_current] > k:
          memo[gi] = (gi_sum, gi_current)
          break;

        gi_sum += g[gi_current]

      else:
        memo[gi] = (sum(g), gi)

      one_loop_index.append(gi)

      s, next_gi = memo[gi]
      euro += s
      gi = next_gi 

    else:
      for ii in xrange(len(one_loop_index)):
        if one_loop_index[ii] == gi:
          one_loop_index = one_loop_index[ii:]
          break
      one_loop_euro = 0
      for euro_index in one_loop_index:
        one_loop_euro += memo[euro_index][0]

      #calculated = i - 1
      calculated = len(one_loop_index)
      #remain = R - calculated
      remain = R - (i-1)

      #euro = euro * (remain/calculated + 1)
      euro += one_loop_euro * (remain/calculated)

      '''
      print 'all', R
      print 'calculated', calculated
      print 'remain', remain
      print 'loopcount', remain/calculated
      print 'euro',euro
      print 'rotate', remain%calculated
      '''

      for k in xrange(remain%calculated):
        s, next_gi = memo[gi]
        #print s
        euro += s
        gi = next_gi 

      break

      

  print 'Case #%d: %d'%(nCase, euro)
