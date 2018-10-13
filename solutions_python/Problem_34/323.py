#!/usr/bin/python

import sys

def check(word, rule):
	i = 0
	for letter in word:
		if isinstance(rule[i], list):
			if letter not in rule[i]:
				return False
		else:
			if letter != rule[i]:
				return False
		i += 1
	return True

words = []

line = sys.stdin.readline().strip()

(L,D,N) = line.split(" ")

for i in range(int(D)):
	line = sys.stdin.readline().strip()
	words.append(line)

X = 1
for line in sys.stdin:
	line = line.strip()
	rule = []
	item = []
	stat = "N"
	for ch in line:	
		if ch == "(":
			item = []
			stat = "P"
		elif ch == ")":
			rule.append(item)
			stat = "N"
		else:
			if stat == "P":
				item.append(ch)
			elif stat == "N":
				rule.append(ch)
	count = 0
	for word in words:	
		result = check(word, rule)
		if result:
			count += 1
	print "Case #%s: %s"%(X,count)
	X += 1
