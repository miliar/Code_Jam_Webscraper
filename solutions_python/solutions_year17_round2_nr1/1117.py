#!/usr/bin/python

def solve(distance, horses):
  maxm_time = -1
  for i in xrange(0, horses):
    pos, speed = [int(s) for s in raw_input().split(" ")]
    time_reqd = (distance - pos) * 1.000000 / speed
    #print "horse {}: pos {}, speed {}, time reqd {}, curr slowest time {}".format(i+1, pos, speed, time_reqd, maxm_time)
    if (time_reqd > maxm_time):
      #print "Im slowest of all times ({})".format(time_reqd)
      maxm_time = time_reqd

  reqd_speed = distance * 1.000000 / maxm_time
  #print "Slowest time is {}, reqd_speed is {}".format(maxm_time, reqd_speed)
  return reqd_speed

def main():
  # read a line with a single integer
  t = int(raw_input())
  for i in xrange(1, t + 1):
    # read a list of integers, 1 in this case
    km, horses = [int(s) for s in raw_input().split(" ")]
    answer = solve(km, horses)
    result = "Case #{0}: {1:.6f}".format(i, answer)
    print result

main()
