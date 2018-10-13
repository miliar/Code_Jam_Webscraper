# -*- coding: utf-8 -*-
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancakes, k = raw_input().split(" ")  # read a list of integers, 2 in this case
  k = int(k)
  pancakes = pancakes.replace("+","1")
  pancakes = pancakes.replace("-","0")
  pancake_length = len(pancakes)
  binary_pancakes = int(pancakes, 2)
  flips = 0
  binary_k = int(math.pow(2, k) - 1)
  # if all pancakes are happy side (+) up, return 0
  if int(math.pow(2, pancake_length) - 1)^binary_pancakes == 0:
	flips = 0
  else:
	  for j in xrange(0,pancake_length - k+1):

		# check the left most pancake, if blank side (-) face up then (ノ°□°)ノ︵ ┻━┻ (flip)
		if binary_pancakes&int(math.pow(2,j)) == 0:
			flips = flips + 1
			binary_pancakes = binary_pancakes^(binary_k << j)
  if int(math.pow(2, pancake_length) - 1)^binary_pancakes != 0:
    flips = "IMPOSSIBLE"
  print "Case #{}: {}".format(i, flips)
	# check out .format's specification for more formatting options