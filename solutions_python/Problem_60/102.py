count = int(raw_input())
for case in range(count):

  # Load input
  N, K, B, T = [int(s) for s in raw_input().split(" ")]
  x0 = [int(s) for s in raw_input().split(" ")]
  v = [int(s) for s in raw_input().split(" ")]

  # Mark who can reach the barn without slow downs
  xt = [ x0[i] + v[i]*T for i in xrange(N) ]
  will_reach = [ i >= B for i in xt ]

  # Start counting chicks and swaps
  k0 = 0
  need_to_swap = 0
  skips = 0
  will_reach.reverse()
  
  for b in will_reach:
    if b:
      skips += need_to_swap
      k0 += 1
      if k0 == K:
        break
    else:
      need_to_swap += 1

  if k0 == K:
    result = str(skips)
  else:
    result = 'IMPOSSIBLE'

  print 'Case #' + str(case+1)  + ': ' + result

  

