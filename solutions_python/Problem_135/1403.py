#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	sys.exit("Usage: " + sys.argv[0] + " <input>")

f = open(sys.argv[1], 'r')

num_tricks = int(f.readline())

for case in range(0, num_tricks):
	a = int(f.readline())
	first = []
	for i in range(0, 4):
		first.append( f.readline().split() )

	b = int(f.readline())
	second = []
	for i in range(0, 4):
		second.append( f.readline().split() )

	count = 0
	same = 0
	for i in first[a-1]:
		if i in second[b-1]:
			count += 1
			same = i

	if count == 1:
		print("Case #" + str(case+1) + ": " + str(same))
	elif count > 1:
		print("Case #" + str(case+1) + ": Bad magician!")
	else:
		print("Case #" + str(case+1) + ": Volunteer cheated!")	
