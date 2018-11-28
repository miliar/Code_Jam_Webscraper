#coding: utf-8
#!/usr/bin/env python2.7
import sys
import copy

def main():
	line = []
	for l in sys.stdin: line.append(l)

	counter = 0
	num = int(line[counter][:-1])
	counter += 1

	for i in range(1, num+1):
		line1 = []
		line2 = []

		first_q = int(line[counter][:-1])
		counter += 1
		line1.append(line[counter][:-1].split())
		counter += 1
		line1.append(line[counter][:-1].split())
		counter += 1
		line1.append(line[counter][:-1].split())
		counter += 1
		line1.append(line[counter][:-1].split())
		counter += 1
		second_q = int(line[counter][:-1])
		counter += 1
		line2.append(line[counter][:-1].split())
		counter += 1
		line2.append(line[counter][:-1].split())
		counter += 1
		line2.append(line[counter][:-1].split())
		counter += 1
		line2.append(line[counter][:-1].split())
		counter += 1

		first_line = line1[first_q-1]
		second_line = line2[second_q-1]

		interset = set(first_line).intersection(second_line)
		len_interset = len(interset)
		if len_interset == 1:
			print 'Case #%s: %s' % (str(i), list(interset)[0])
		elif len_interset == 0:
			print 'Case #%s: Volunteer cheated!' % (str(i))
		else:
			print 'Case #%s: Bad magician!' % (str(i))

if __name__ == '__main__':
	main()


