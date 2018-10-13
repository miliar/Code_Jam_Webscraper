#!/usr/bin/env python3

from sys import *
from math import *

def calc_minutes(plates):
	return max(plates)

def solve(D, plates):
	D = D.strip("\n")
	plates = plates.strip("\n")
	plates = [int(x) for x in plates.split(" ")]
	plates_ninesplit = plates
	old_mins = 1000
	extra_mins = 0
	mins_history = []
	for x in range(max(plates)):
		mins = calc_minutes(plates) + extra_mins
		mins_history.append(mins)
		M = max(plates)
		n = plates.count(M)
		plates = [ceil(y/2) if y == M else y for y in plates]
		for z in range(n):
			plates.append(floor(M/2))
		extra_mins += n
	extra_mins = 0
	for x in range(max(plates_ninesplit)):
		mins = calc_minutes(plates_ninesplit) + extra_mins
		mins_history.append(mins)
		M = max(plates_ninesplit)
		n = plates_ninesplit.count(M)
		if(M == 9):
			plates_ninesplit = [3 if y == M else y for y in plates_ninesplit]
			for z in range(n):
				plates_ninesplit.append(6)
		else:
			plates_ninesplit = [ceil(y/2) if y == M else y for y in plates_ninesplit]
			for z in range(n):
				plates_ninesplit.append(floor(M/2))
		extra_mins += n
	return str(min(mins_history))

def main():
	counter = int(stdin.readline())
	for x in range(counter):
		output = solve(stdin.readline(), stdin.readline())
		print('Case #' + str(x + 1) + ': ' + output)

if __name__ == "__main__":
	main()
