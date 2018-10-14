#!/usr/bin/env python

import sys

def is_pal( num ):
	s = str(num)
	return s == s[::-1]

def is_FS( num ):
	return False
	
def iter_up( s ):
#	print "iter"
	r = []
	for x in range(1,10):
		for y in s:
			r.append(int(str(x)+str(y)+str(x)))
	return r


def solve( lower, higher, FSs, p_ws, hp, hf ):
	'''
	IN: range of numbers to check if fairsquares
	OUT: # of fair squares, the known set and set limits

	If the higher range is higher than hf(highest known ffs) update the set to sqrt(higher)
	else check membership of range
	'''
	count = 0
	new_hp = hp
	new_hf = hf
	if( higher > hf ):
		new_hf = (higher+1)**.5
		while( new_hp < new_hf ):
			for x in p_ws:
				parent = x*x
				if( is_pal(parent) ):
#					print "Adding",parent
					FSs.append(parent)
			p_ws = iter_up(p_ws)
			new_hp = p_ws[0]
			if 12345678987654321 in FSs:
				break
	
	for x in FSs:
		if x >= lower and x < higher+1:
			count += 1

	return (FSs, count, new_hp, new_hf, p_ws)

def run():
	if len(sys.argv) < 2:
		print "Missing arg"
	else:
		f = open(sys.argv[1],'r')
		data = f.read().split("\n")
		f.close()
		number_of_tests = int(data[0])
		known_fs = []
		working_set = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
		highest_pals = 1
		highest_fss = 1
		for x in range(number_of_tests):
			test_s = data[x+1].split(" ")
			lower = int(test_s[0])
			higher = int(test_s[1])
			res = solve( lower, higher, known_fs, working_set, highest_pals, highest_fss )
			known_fs = res[0]
			highest_pals = res[2]
			highest_fss = res[3]
			working_set = res[4]
			print "Case #" + str(x+1) + ": " + str(res[1])


if __name__ == "__main__":
	run()
