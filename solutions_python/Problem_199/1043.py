# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# Problem A. Oversized Pancake Flipper

import numpy as np

#solution: give a input string, and a number, return the minitime of times
# required to filip the cake, otherwise return "IMPOSSIBLE"
def solution(s, t):
    #return something

    l_s = map(lambda x: 1 if x == "+" else 0, list(s))
    #print l_s
    t_container = np.array(l_s)
    #print t_container
    # do flipper
    result = 0
    for i in xrange(t_container.size - t + 1):
        if t_container[i] != 1:
            #do flip
            result += 1
            t_container[i:i+t] = 1 - t_container[i:i+t]
            #print t_container, result

        else:
            continue
    if all(t_container[-t:] == 1):
        return result
    else:
        return "IMPOSSIBLE"

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #t_s : ---++---   cake formation
  #t_t : 3
  t_s, t_t = raw_input().split(" ")
  t_t = int(t_t)

  #do Solution:
  #
  result = solution(t_s, t_t)

  #print "Case #{0}: {1} {2)".format(i, n + m, n * m)
  print "Case #{0}: {1}".format(i, result)
  # check out .format's specification for more formatting options


