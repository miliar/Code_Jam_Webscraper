import sys
import os

def solve(list_pancakes, k):
	ind_start = 0
	nb_flips = 0
	n = len(list_pancakes)
	while(True):
		# print("ind_start : ", ind_start)
		# print("list_pancakes : ", list_pancakes)
		# print("nb_flips : ", nb_flips)
		if not('-' in list_pancakes):
			return nb_flips
			break
		# Ptet n-k-1, je sais plus
		if (ind_start > n-k):
			return -1
			break

		# print(list_pancakes[ind_start])
		if list_pancakes[ind_start] == '-':
			nb_flips += 1
			for j in range(k):
				if (list_pancakes[ind_start+j]=='-'):
					list_pancakes[ind_start+j]='+'
				else:
					list_pancakes[ind_start+j]='-'

		ind_start += 1

t = int(input())


for i in range(t):
	s, k = input().split()
	k = int(k)
	sol = solve(list(s),k)

	print("Case #" + str(i+1) + ": ", end="")
	print("IMPOSSIBLE") if sol==-1 else print(sol)