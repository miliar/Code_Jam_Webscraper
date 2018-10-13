#!/usr/bin/python

import sys

def test(mat,k,color):
	for i in xrange(len(mat)):
		curr_strike = 0
		for j in xrange(len(mat)):
			if mat[j][i] != color:
				curr_strike = 0
			else:
				curr_strike += 1
				if curr_strike == k:
					return True 
        
	for i in xrange(len(mat)):
		curr_strike = 0
		for j in xrange(len(mat)):
			if mat[i][j] != color:
				curr_strike = 0
			else:
				curr_strike += 1
				if curr_strike == k:
					return True 
	for i in xrange(len(mat)):
		for j in xrange(len(mat)):
			curr_strike = 0
			for x in xrange(k):
				if i+x >= len(mat) or j+x >= len(mat) or mat[i+x][j+x] != color:
					curr_strike = 0
				else:
					curr_strike += 1
					if curr_strike == k:
						return True 
	for i in xrange(len(mat)):
		for j in xrange(len(mat)):
			curr_strike = 0
			for x in xrange(k):
				if i+x >= len(mat) or j-x < 0 or mat[i+x][j-x] != color:
					curr_strike = 0
				else:
					curr_strike += 1
					if curr_strike == k:
						return True 
	return False

def handle_case(mat,k):
	for i in range(len(mat)):
		mat[i] = mat[i].replace(".", "")
		mat[i] = "".join(["."]*(len(mat)-len(mat[i]))) + mat[i]
           
	red_can = test(mat,k, "R")
	blue_can = test(mat,k, "B")

	if red_can and not blue_can:
		return "Red"

	if not red_can and blue_can:
		return "Blue"

	if red_can and blue_can:
		return "Both"
       
   
	return "Neither"

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(n,k) = map(int,fsock.readline().rstrip("\n").split(" "))
		mat = []
		for i in xrange(n):
			mat.append(fsock.readline().rstrip("\n"))
		print "Case #%d: %s" % (case, handle_case(mat,k))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

