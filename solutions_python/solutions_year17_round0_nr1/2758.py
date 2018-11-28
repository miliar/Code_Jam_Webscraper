
if __name__ == "__main__":
  # read input
  t = int(raw_input())
  for i in xrange(1, t + 1):
 	pancakes, flipper = raw_input().split(" ")
	pancakes = list(pancakes)
	flipper = int(flipper)
	flips = 0
	# we'll go through each pancake and make a flip if the pancake is not correct
	for c in xrange(0, len(pancakes)):
		if (pancakes[c] != '+'):
			if (c + flipper > len(pancakes)):
				flips = "IMPOSSIBLE"
				break
			for j in xrange(0, flipper):
				pancakes[c+j] = '-' if pancakes[c+j] == '+' else '+'
			flips = flips + 1
	print "Case #{}: {}".format(i, flips)
