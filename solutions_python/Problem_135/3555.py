#!/usr/bin/env python
# -*- coding: utf-8 -*-

def testcase(tc):
	a = int(raw_input())-1
	lines = []
	for i in range(4):
		line = raw_input().split(' ')
		line = map(int, line)
		lines.append(line)
	linea = set(lines[a])
	
	b = int(raw_input())-1
	lines = []
	for i in range(4):
		line = raw_input().split(' ')
		line = map(int, line)
		lines.append(line)
	lineb = set(lines[b])
	inter = linea & lineb
	x = len(inter)
	ans = ""
	if x==0 : ans = "Volunteer cheated!"
	elif x==1 : ans = "%d" % (inter.pop(),)
	else : ans = "Bad magician!"
	print "Case #%d: %s" % (tc+1, ans)



if __name__ == "__main__":
	n = int(raw_input())
	for i in range(n):
		testcase(i)

