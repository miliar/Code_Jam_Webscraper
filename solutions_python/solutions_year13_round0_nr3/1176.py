# Python 2.7.2 (341e1e3821fff77db3bb5cdb7a4851626298c44e, Nov 23 2012, 19:06:15)
# [PyPy 1.9.0] on darwin
# (C) 2013 Dennis Bliefernicht

BASENAME="C"
TYPE="ex"
TYPE="sm5"
#TYPE="la"
NODOUT=False

import math

c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def pal_check(i, min, max):
	sq = i * i
	print i, sq
	if sq < min or sq > max:
		return 0
	
	sqs = str(sq)
	first = sqs[:(len(sqs)+1)/2]
	last = sqs[len(sqs)/2:]
	last = last[::-1]
	if first == last:
		return 1
	return 0

def check_pals(prefix, l, min, max):
	if l <= 0:
		rev = prefix[::-1]
		c1 = long(prefix + rev)
		c2 = long(prefix + rev[1:])
		return pal_check(c1, min, max) + pal_check(c2, min, max)
	else:
		sum = 0
		for ch in c:
			sum += check_pals(prefix + ch, l - 1, min, max)
		return sum

def is_pal(x):
	s1 = str(x)
	s2 = s1[::-1]
	return s1 == s2

def process():
	(min, max) = popintarray()
	
	minlen = len(str(min)) / 2 
	maxlen = len(str(max)) / 2 + 1
	
	sum = 0
#	for l in range(minlen, maxlen+1):
#		for ch in c[1:]:
#			sum += check_pals(ch, l - 1, min, max)

	for x in range(min, max+1):
		if is_pal(x):
			r = int(math.sqrt(x))
			if r * r == x and is_pal(r):
				sum += 1
	
	return str(sum)

# ------------------------------------
# GCJ2013 framework stuff
# ------------------------------------
import time

lines = []
outf = None

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def popintarray():
	return map(lambda x: int(x), pop().split(" "))

def popstrarray():
	return pop().split(" ")
	
def outstr(s):
	global outf
	print s
	outf.write(s + "\n")

def dout(*vals):
	if NODOUT:
		return
	print "%",
	for v in vals:
		print str(v),
	print
	
def main():
	global lines
	case_count = int(pop())
	for case_number in range(case_count):
		result = process()
		outstr("Case #%d: %s" % (case_number+1, result))
	if len(lines) != 0:
		print "! %d lines remaining" % (len(lines))

if __name__ == "__main__":
	fname = BASENAME
	if TYPE[0:2] == "sm":
		fname += "-small"
		if len(TYPE) > 2:
			fname += "-attempt" + TYPE[2:]
	elif TYPE == "la":
		fname += "-large"

	f = open(fname + ".in", "r")
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	
	outf = open(fname + ".out", "w")
	timebefore = time.time()
	main()
	timeafter = time.time()
	outf.close()
	
	runtime = timeafter - timebefore
	print "%% Runtime: %dm%2.3fs" % (int(runtime / 60), runtime % 60)
	