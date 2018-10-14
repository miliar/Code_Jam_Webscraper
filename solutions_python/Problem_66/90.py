#!/usr/bin/python

import sys

def build_tree(n):
	if n == 0:
		return None
	else:
		return [False, build_tree(n-1), build_tree(n-1)]
	
def get_bit(n,pos):
	return (n%(2**(pos+1)))/(2**(pos))

def sum_true(tree):
	if tree is None or not tree[0]:
		return 0
	else:
		return 1 +  sum_true(tree[1]) + sum_true(tree[2])

def handle_case(P, cons, price):
	tree = build_tree(P)
	for i, k in enumerate(cons):
		curr_sub_tree = tree
		for j in xrange(P-k):
			curr_sub_tree[0] = True
			curr_sub_tree = curr_sub_tree[1+get_bit(i,P-j-1)]
	return sum_true(tree)

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		P = int(fsock.readline())
		cons = map(int,fsock.readline().rstrip("\n").split(" "))
		price = []
		for i in xrange(P):
			price.append(map(int,fsock.readline().rstrip("\n").split(" ")))
		print "Case #%d: %d" % (case, handle_case(P, cons, price))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

