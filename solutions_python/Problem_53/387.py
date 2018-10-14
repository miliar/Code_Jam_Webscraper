#!/usr/bin/python

import sys

def handle_case(n,k):
    if (k % (2**n)) != ((2**n)-1):
        return "OFF"
    else:
        return "ON"

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(n,k) = map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %s" % (case, handle_case(n,k))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

