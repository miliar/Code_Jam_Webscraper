#!/usr/bin/python

import sys

def handle_case(exist, create):
	tree = {}
	tree[""] = {}

	for path in exist:
		sections = path.split("/")
		curr_loc = tree
		for section in sections:
			if section not in curr_loc:
				curr_loc[section] = {}
			curr_loc = curr_loc[section]

	sections_to_add = 0
	for path in create:
		sections = path.split("/")
		curr_loc = tree
		for section in sections:
			if section not in curr_loc:
				curr_loc[section] = {}
				sections_to_add += 1
			curr_loc = curr_loc[section]
	return sections_to_add

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(N,M) = map(int,fsock.readline().rstrip("\n").split(" "))
		exist = []
		for i in xrange(N):
			exist.append(fsock.readline().rstrip("\n"))
		create = []
		for i in xrange(M):
			create.append(fsock.readline().rstrip("\n"))
		print "Case #%d: %d" % (case, handle_case(exist, create))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

