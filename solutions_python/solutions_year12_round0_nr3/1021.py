import math

rec_list_a = []
rec_list_b = []

f = open('C-small.in', 'r')
lines = f.readlines()

def rec(num, A, B):
	num_s = str(num);
	for i in range(len(num_s) - 1, 0, -1):
		r = num_s[i:] + num_s[:i]

		if not (r in rec_list_a and num_s in rec_list_b):
			if not (r in rec_list_b and num_s in rec_list_a):
				if not r[0] == '0' and not r == num_s:
					r_i = int(r)
					if r_i >= A and r_i <= B:
						rec_list_a.append(num_s)
						rec_list_b.append(r)

A = 0
B = 0
for i in range(1, len(lines)):
	line = lines[i].split('\n')[0].split(' ')
	A = line[0]
	B = line[1]
	rec_list_a = []
	rec_list_b = []
	for j in range(int(A), int(B) + 1):
		rec(j, int(A), int(B))
	print "Case #" + str(i) + ": " + str(len(rec_list_a))
