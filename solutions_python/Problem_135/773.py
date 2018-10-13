"""Code written using Python 2.7.5, http://www.python.org/"""

import string

def compare(row1, row2):
	nums1 = [int(e) for e in row1.split()]
	nums2 = [int(e) for e in row2.split()]
	result = []
	for n in nums1:
		if n in nums2:
			result += [n]

	if len(result) == 1:
		return result[0]
	elif len(result) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"
	

def calc(case):
	row1 = int(case[0])
	row2 = int(case[5])
	arr1 = case[1:5]
	arr2 = case[6:]
	return compare(arr1[row1-1], arr2[row2-1])


f = open('A-small.in', 'r')
lines = f.readlines()
f.close()
c = int(lines[0].split()[0])
#print c
cases = [r.strip() for r in lines[1:]]
#print cases

of = open('output_a_small.txt', 'w')

for idx in range(0, c):
	of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(cases[idx*10:idx*10 + 10])})

of.close()

