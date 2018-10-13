# from __future__ import print_function 
import os
import sys


def smallest_tidy_n(n_str):
	# for the single digit special case
	if len(n_str) == 1:
		return n_str

	# special case: identical digits
	if n_str == n_str[0] * len(n_str):
		return n_str

	# for the special case of something like:
	# 110, 101, 100
	# ( answer in these cases is 99)
	for i in range(len(n_str)):
		if int(n_str[i]) > 1 :
			break

		if i == len(n_str)-1:
			return "9" * (len(n_str) - 1)

	res = n_str[0]
	for i in range(len(n_str)-2, -1, -1):

		if int(n_str[i+1]) < int(n_str[i]):
			# print(12312312)
			return smallest_tidy_n( n_str[0:i] + str(int(n_str[i])-1) + "9" * (len(n_str)-i-1) )
			
	return n_str

def remove_trailing_zeros(n_str):
	start = 0
	for i in range(len(n_str)):
		if n_str[i] == '0':
			start = i+1
			break

	return n_str[start:]

f = open(sys.argv[1])
outf = open(sys.argv[1] + ".out", 'w')

n = int(f.readline())
#
for nth in range(n):

	num_str = f.readline().strip()
	tidy = smallest_tidy_n(num_str)
	tidy = remove_trailing_zeros(tidy)

	res = "Case #%d: %s" % (nth+1, tidy)
	# print(num_str)
	# print(res)

	if nth < n-1:
		res = res + "\n"
	outf.write(res)
