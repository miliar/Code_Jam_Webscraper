def solve(A, motes, num, times):
  if num >= len(motes):
    return times
  if motes[num] < A:
    return solve(A+motes[num], motes, num+1, times)
  elif A != 1:
    return min(solve(2*A-1, motes, num, times+1), solve(A, motes, num+1, times+1))
  else:
    return solve(A, motes, num+1, times+1)

times  = int(raw_input())
for time in xrange(times):
  A,N = map(int,raw_input().split())
  motes = map(int,raw_input().split())
  count = 0
  cur = A
  motes.sort()
  print "Case #%d:" % (time+1), solve(cur, motes, 0, 0)
      

      
