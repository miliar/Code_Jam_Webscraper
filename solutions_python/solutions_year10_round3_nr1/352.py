import sys
import re

fin = open('input.in', 'r')
fout = open('output.out', 'w')
nos = long(fin.readline().strip())
for case in range(nos):
	no_lines = long(fin.readline().strip())
	inters = 0
	inters_list = []
	points = []
	inters_add = 0
	for temp in range(no_lines):
		temp_line = (fin.readline().strip()).split(" ")
		points.append(temp_line)
	for temp1 in points:
		A = long(temp1[0])
		B = long(temp1[1])
		inters = 0
		for temp2 in points:
			a = long(temp2[0])
			b = long(temp2[1])
			if a < A and b < B:
				#do nothing
				inters = inters
			elif a > A and b > B:
				#do nothing
				inters = inters
			elif a < A and b > B:
				inters = inters+1
			elif a > A and b < B:
				inters = inters+1
		inters_list.append(inters)
		inters_add = inters_add + inters
	print inters_list
	print inters_add
	fout.write('Case #%(case)d: %(inters_add)d' % {'case':(case+1), 'inters_add':(inters_add/2)})
	print case," ",nos
	if case+1 != nos:
		fout.write('\n')

fout.close()
fin.close()