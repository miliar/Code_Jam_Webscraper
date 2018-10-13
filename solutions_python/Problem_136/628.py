# (k - 1) * F + 2   = r_{k-1}
#     k   * F + 2   = r_k
# X/r_{k-1} > C/r_{k-1} + X/r_k
# X * r_k > C * r_k + X * r_{k-1}
# (X - C) * r_k > X * r_{k-1}
# (X - C)/X > r_{k-1}/r_k
import sys

def shouldBuildFarm(k):
  return (target - farm_cost) * (k * rate_delta + 2) > target * ( (k-1) * rate_delta + 2 )

sys.stdin  = open("B-large.in")
sys.stdout = open("B-large.out", "w")
t = int(raw_input())
for case_no in range(1, t+1):
  farm_cost, rate_delta, target = map(float, raw_input().split())
  # find number of times we need to buy the farm
  lo, hi = 0, 100000
  while lo + 1 < hi:
    mid = (lo + hi)/2
    if shouldBuildFarm(mid):
      lo = mid
    else:
      hi = mid - 1
  if (lo + 1 == hi) and not shouldBuildFarm(hi):
    hi = lo
  # calculate the total time to win
  ans = 0.0
  rate = 2
  for i in range(hi):
    ans += farm_cost/rate
    rate += rate_delta
  ans += target/rate
  print "Case #%d: %f" % (case_no, ans)