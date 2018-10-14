#!/usr/bin/python

import sys

def handle_case(case_no, times_from_A, times_from_B):
	new_A = [0]
	new_B = [0]
	wait_at_A = []
	wait_at_B = []

	map(lambda x: x.append("A"), times_from_A)
	map(lambda x: x.append("B"), times_from_B)
	unite  = times_from_A + times_from_B

	unite.sort(s_by_start_end)

	for l in unite:
		if l[2] == 'A':
			make_train(l, new_A, wait_at_A, wait_at_B)
		else:
			make_train(l, new_B, wait_at_B, wait_at_A)

	print "Case #%d: %d %d" % (case_no, new_A[0], new_B[0])

def make_train(train, counter, from_list, to_list):
	if len(from_list)==0 or train[0] < from_list[0]:
		counter[0] += 1
	else:
		del from_list[0]

	to_list.append(train[1])
	to_list.sort()

def s_by_start_end(i1, i2):
	if i1[0] < i2[0] or (i1[0] == i2[0] and i1[1] <= i2[1]):
		return -1
	else:
		return 1

def in_minutes(str):
	(h,m) = map(int, str.split(":"))
	return h*60+m

def main():
        filename = sys.argv[1]
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		turnaround = int(fsock.readline())
		(NA, NB) = map(int, fsock.readline().rstrip("\n").split(" "))
		times_from_A = []
		for ta in range(1,NA+1):
			line = map(in_minutes, fsock.readline().rstrip("\n").split(" "))
			times_from_A.append(line)

		times_from_B = []
	        for tb in range(1,NB+1):
			line = map(in_minutes, fsock.readline().rstrip("\n").split(" "))
			times_from_B.append(line)

		for t in times_from_A:
                	t[1] += turnaround
	        for t in times_from_B:
        	        t[1] += turnaround
			
		handle_case(case, times_from_A, times_from_B)
	fsock.close()


if __name__ == "__main__":
    main()

