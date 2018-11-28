#!/usr/bin/env python2

import sys

def friends_needed(audience):
	friend_count = 0
	clapping_count = int(audience[0])
	for i, a in enumerate(map(int, audience[1:]), start=1):
		if clapping_count >= i:
			clapping_count += a
		else:
			needed = i - clapping_count
			friend_count += needed
			clapping_count += needed + a
	return friend_count

if __name__ == "__main__":
	infile = file(sys.argv[1], "r")
	outfile = file(sys.argv[2], "w")

	index = 0
	for line in infile:
		if index == 0:
			index += 1
			continue
		_, audience = line.strip().split(" ")
		outfile.write("Case #%s: %s\n" % (index, friends_needed(audience)))
		index += 1

	infile.close()
	outfile.close()
