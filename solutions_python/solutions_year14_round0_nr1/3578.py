#!/usr/bin/python

import sys

def find_card(row1, matrix1, row2, matrix2):
	s1=set(matrix1[row1-1])
	s2=set(matrix2[row2-1])
	intersection = list(s1 & s2)
	if len(intersection) == 1:
		return "%d"%(intersection[0])
	elif len(intersection) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"

def input():
	vrow = int(sys.stdin.readline())
	j = 0
	matrix = []
	while(j<4):
		row = map(int, sys.stdin.readline().split(" "))
		matrix.append(row)
		j += 1
	return (vrow, matrix)
	
if __name__ == "__main__":
	T=int(sys.stdin.readline())
	i = 0
	while(i < T):
		i += 1
		r1, m1 = input()
		r2, m2 = input()
		print("Case #%d: %s"%(i, find_card(r1,m1,r2,m2)))
