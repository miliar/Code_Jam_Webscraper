import sys
import math

T = int(sys.stdin.readline().strip())

def area(r):
  return math.pow(r, 2)


for case in range(0,T):

  r, t = map(int, sys.stdin.readline().strip().split(" "))

  def run():
    starting_area = math.pow(r, 2)
    can_draw_area = t
    remaining = can_draw_area
    cnt = 0
    while remaining >= 0:
      remaining -= area(r+cnt*2+1) - area(r+cnt*2)
      cnt += 1
    return cnt - 1

  ans = run()

  print "Case #%d: %s" % (case + 1, ans)