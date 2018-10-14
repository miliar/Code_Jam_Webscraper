#!/usr/bin/env python

def magic(firstlayout,secondlayout,firstanswer,secondanswer):
	assert firstanswer in (1,2,3,4)
	assert secondanswer in (1,2,3,4)
	firstrow = firstlayout[firstanswer-1]
	secondrow = secondlayout[secondanswer-1]
	u = set(firstrow).intersection(secondrow)
	if len(u) == 1:
		return u.pop()
	if len(u) > 1:
		return "Bad magician!"
	return "Volunteer cheated!"


if __name__ == "__main__":
	import sys
	testcases = int(sys.stdin.readline())
	for casenum in range(testcases):
		first_layout,second_layout = [],[]
		first_answer = int(sys.stdin.readline())
		for n in range(4):
			first_layout.append(map(int,sys.stdin.readline().split()))
		second_answer = int(sys.stdin.readline())
		for n in range(4):
			second_layout.append(map(int,sys.stdin.readline().split()))
		print "Case #%s:" % (casenum+1,),magic(first_layout,second_layout,first_answer,second_answer)
