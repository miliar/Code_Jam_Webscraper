import sys
import re
import math

pi = math.pi


def draw_possible(count,r,t):
	if t < 0:
		return count

	while t > 0 or t == 0:
		t = t - ((r+1)**2 - r**2)
		r += 2
		count += 1

	return count-1




def main(file):
	f = open(file, 'r')
	howmany = int(f.readline()) # how many test cases are there?
	stage = 0

	fo = open('A-small-attempt0.out', 'wd')
	
	while stage < howmany:
		given = f.readline().split()
		r,t = int(given[0]), int(given[1])
		count = 0
		print r,t

		count = draw_possible(count,r,t)
		print count

		stage += 1
		fo.write("Case #" + str(stage) + ": " + str(count) + "\n")

if __name__ == '__main__':
	main('A-small-attempt0.in')





















