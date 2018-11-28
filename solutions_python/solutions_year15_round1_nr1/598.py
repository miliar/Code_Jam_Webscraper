T = input()
for case in xrange(T):
  N = input()
  nums = map(int, raw_input().split())

  first = 0
  maxdiff = 0
  for i in xrange(1, len(nums)):
    if nums[i] < nums[i-1]:
      first += nums[i-1] - nums[i]
      maxdiff = max(maxdiff, nums[i-1] - nums[i])

  second = 0
  for i in xrange(len(nums)-1):
    second += min(maxdiff, nums[i])

  print "Case #%d: %d %d" % (case+1, first, second)