import sys, os

f = open('C-input.in', 'r')
fout = open('C-out', 'w')
case_cnt = int(f.readline())


for i in range(case_cnt):
	f.readline()
	l = f.readline()
	el = l.split()
	el_num = []
	for e in el:
		el_num.append(int(e))

	el_num.sort()
	total = 0

	for e in el_num:
		total ^= e;
	
	if total != 0:
		fout.write('Case #%d: NO\n' % (i + 1,))
		continue
	
	el_num = el_num[1:]

	total = sum(el_num)
	fout.write('Case #%d: %d\n' % (i + 1, total))
