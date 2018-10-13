#!/usr/bin/python

import sys

def handle_case(R,k,g):

    everything = sum(g)
    if everything <= k:
       return everything * R

    rev = 0
    ptrs = [None]*len(g)
    curr_pos = 0
    while R > 0 and ptrs[curr_pos] is None:
       curr_load = 0
       next_pos = curr_pos
       while curr_load +  g[next_pos] <= k:
          curr_load += g[next_pos]
          next_pos = (next_pos + 1) % len(g)
       ptrs[curr_pos] = [curr_load, next_pos]
       R -= 1
       rev += curr_load
       curr_pos = next_pos
    if R == 0:
       return rev
    cars_for_cycle = 1
    cycle_rev = ptrs[curr_pos][0]
    tmp_pos = ptrs[curr_pos][1]
    while tmp_pos != curr_pos:
      cars_for_cycle += 1
      cycle_rev += ptrs[tmp_pos][0]
      tmp_pos = ptrs[tmp_pos][1]
    rev += cycle_rev * (R/cars_for_cycle)

    R %= cars_for_cycle
    while R > 0:
       R -= 1
       rev += ptrs[curr_pos][0]
       curr_pos = ptrs[curr_pos][1]
    return rev

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(R,k,N) = map(int,fsock.readline().rstrip("\n").split(" "))
		g = map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %d" % (case, handle_case(R,k,g))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

