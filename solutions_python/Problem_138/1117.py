#!/usr/bin/python3

def war (she, he):
	win = 0
	tmp_she = list(she)
	tmp_he = list(he)
	for e1 in tmp_she:
		for e2 in tmp_he:
			if (e2 > e1):
				tmp_he.remove(e2)
				break
		else:
			win += 1
	return win

def cheating (she, he):
	win = 0
	tmp_she = list(she)
	tmp_he = list(he)
	for i, e1 in enumerate(tmp_she):
		cnt = 0
		for e2 in tmp_he:
			if (e2 < e1):
				cnt += 1 
			else:
				break
		if (cnt-win > 0):
			win += 1
	return win

t = input()
t = int(t)
for test in range(t):
	cnt = int(input())
	she = [float(x) for x in input().split(" ")]
	he = [float(x) for x in input().split(" ")]
	she.sort()
	he.sort()
	print ("Case #%d: %d %d" % (test+1, cheating(she, he), war(she, he)))