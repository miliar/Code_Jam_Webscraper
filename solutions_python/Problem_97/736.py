#!/usr/bin/python
import sys

def calculate_rotations(min, max):
	rotations = set()
	for i in xrange(min, max+1):
		current = str(i)
		for j in xrange(1,len(current)):	
			alt = current[j:] + current[0:j]
			
			current_i = int(current)
			alt_i = int(alt)
			if (current_i < alt_i):
				k = (current_i,alt_i)
			else:
				k = (alt_i,current_i)

			if (alt_i != current_i and alt_i >= min and alt_i <= max and k not in rotations):
				rotations.add(k)

	return len(rotations)

def main():
	T = int(sys.stdin.readline())
	
	for i in xrange(T):
		line = sys.stdin.readline().strip()
		parts = line.split(' ')
		min = int(parts[0])
		max = int(parts[1])
		if (min < 10):
			value = 0
		else:
			value = calculate_rotations(min,max)
		
		print "Case #" + str(i+1) + ": " + str(value)
main()
