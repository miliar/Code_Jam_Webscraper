def annie_speed(D, N, distances, speeds):
  distances.sort(reverse=True)
  time = (D - distances[0])/1.0/speeds[distances[0]]
  for i in range(1, N):
    catchuptime = will_catch_up_in(distances[i-1], distances[i], speeds[distances[i-1]], speeds[distances[i]], time)
    if catchuptime < 0 or catchuptime > time:
      time = (D-distances[i])/1.0/speeds[distances[i]]

  return D/time


def will_catch_up_in(d1, d2, s1, s2, time):
  if s2 <= s1:
    return -1
  return (d1-d2)/1.0/(s2-s1)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  D, N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this 
  distances = []
  speeds = {}
  for j in xrange(0, N):
    d, s = [int(s) for s in raw_input().split(" ")]
    distances.append(d)
    speeds[d] = s
  print "Case #{}: {}".format(i, annie_speed(D, N, distances, speeds))
  # check out .format's specification for more formatting options
