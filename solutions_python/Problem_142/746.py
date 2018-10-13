from copy import deepcopy
import plex

from mpmath import *
mp.dps = 20
import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0


t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

def debug(message):
	if sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

def split_sections(s):
	sections = []
	previous_char = None
	for char in s:
		if char != previous_char:
			sections.append({"c":char,"n":0})
		previous_char = char
		sections[-1]["n"] += 1
	return sections

def min_changes(strings):
	N = float(len(strings))
	debug("got %d strings" % N)
	s1 = strings[0]
	ch = 0
	for i in xrange(len(s1)):
		counts = []
		for string in strings:
			if len(string) != len(s1):
				return "Fegla Won"
			if string[i]["c"] != s1[i]["c"]:
				debug("failed at %d" % i)
				return "Fegla Won"
			counts.append(string[i]["n"])
		avg = int(sum(counts) / N)
		ch += sum(map(lambda x: abs(x-avg), counts))
	return ch

for tc in xrange(t):
	debug("case: %d" % (tc+1))
	n = int(inp.readline())
	s = []
	for i in xrange(n):
		s.append(split_sections(inp.readline().strip()))
	
	print_case(tc+1,min_changes(s))
	
	