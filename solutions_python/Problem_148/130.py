
for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  N, X = map(int, raw_input().split())
  nums = map(int, raw_input().split())
  assert len(nums) == N
  nums.sort()
  ans = 0
  while nums:
    x = nums.pop()
    ans += 1
    if not nums:
      break
    if nums[0] + x <= X:
      nums.pop(0)
  print ans
