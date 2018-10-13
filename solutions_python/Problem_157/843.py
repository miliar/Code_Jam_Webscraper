#coding: utf-8
#! /usr/bin/env python2.7

import sys
import re

def rule(a,b):
	if a+b == "ij": 
		return "k", 1
	elif a+b == "ji": 
		return "k", -1
	elif a+b == "ki":
		return "j", 1
	elif a+b == "ik":
		return "j", -1
	elif a+b == "jk":
		return "i", 1
	elif a+b == "kj":
		return "i", -1
	elif a == b:
		return "1", -1
	elif a == "1":
		return b, 1
	elif b == "1":
		return a, 1

def sub(string, inputflag):
#	print input_strings, l, r
	flag = inputflag
	while len(string) >= 2:
#		print len(string), string
		string = string.replace("ij","k")
		string = string.replace("ki","j")
		string = string.replace("jk","i")

		tmpstring = string.replace("ji","k")
		tmpstring = tmpstring.replace("ik","j")
		tmpstring = tmpstring.replace("kj","i")
		if tmpstring != string:
			flag *= (-1) ** (len(string)-len(tmpstring))
			string = tmpstring

		tmpstring = string.replace("ii","")
		tmpstring = tmpstring.replace("jj","")
		tmpstring = tmpstring.replace("kk","")
		if tmpstring != string:
			flag *= (-1) ** ((len(string)-len(tmpstring))/2)
			string = tmpstring


#	print string, flag
	if string == "j" and flag == 1: return True, string, flag
	else: return False, string, flag


def match(string, goal):
	result_list = []
	now = string[0]
	now_flag = 1
	if now == goal:
		result_list.append(0)
	for i in range(1,len(string)):
		s = string[i]
		new, flag = rule(now, s)
		now = new
		now_flag *= flag
		if now == goal and now_flag == 1:
			result_list.append(i)
	return result_list

def reverse_match(string, goal):
	result_list = []
	now = string[-1]
	now_flag = 1
	if now == goal:
		result_list.append(len(string)-1)
	for i in range(len(string)-2,-1,-1):
		s = string[i]
		new, flag = rule(s, now)
		now = new
		now_flag *= flag
		if now == goal and now_flag == 1:
			result_list.append(i)
	result_list.sort(reverse=True)
	return result_list

def main():
	line = []
	for l in sys.stdin:
		line.append(l[:-1])

	c = 0
	T = int(line[c])

	c += 1
	for i in range(T):
		snum, srepeat = map(int, line[c].strip().split())
		c += 1
		string = line[c].strip()
		strings = string*srepeat
		c += 1

		if len(strings) < 3:
			print "Case #%d: NO" % (i+1)
			continue

		left_list = match(strings, "i")
		right_list = reverse_match(strings, "k")

		flag = 0
		for l in left_list:
			prev = ""
			prev_string = ""
			prev_r = l+1
			dflag = 1
			for r_index in range(len(right_list)):
				if r_index != 0:
					prev_r = right_list[r_index-1]
				r = right_list[r_index]
				if l >= r: break
#				print l,r, strings[l+1:r], prev_string+strings[prev_r:r]
				flag, prev_string, dflag = sub(prev_string+strings[prev_r:r], dflag)
				if flag: break
			if flag: break
		if flag: print "Case #%d: YES" % (i+1)
		else: print "Case #%d: NO" % (i+1)

if __name__ == "__main__":
	main()
