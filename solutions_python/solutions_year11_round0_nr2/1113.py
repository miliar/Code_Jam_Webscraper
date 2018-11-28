import re
import sys

def parse (ip):
	pairs = {}
	opposed = []
	cnt = 0
	regex = re.compile (" *\d+ *(.*) *\d+ +(.*) *\d+ *(.*)$")
	mch = regex.match (ip)
	_pairs, _opposed, _ip = mch.groups ()
	for p in _pairs.split ():
		pairs [p [:2]] = p[2]
	opposed = _opposed.split ()
	return pairs, opposed, _ip

def get_prev (op):
	if op:
		return op [-1]
	return None

def get_pairs (a, b, pairs):
	strs = [a+b, b+a]
	for s in strs:
		for p in pairs:
			if p == s:
				return pairs [p]
	return None

def substitute_op (op, repl):
	op = op [:-1]
	op [-1] = repl
	return op


def check_for_opposeds (x, op, opposeds):
	for e in op [:-1]:
		if e+x in opposeds or x+e in opposeds:
			return True
	return False

def solve (ip):
	op = []
	print >> sys.stderr, ip
	pairs, opposed, ip = parse (ip)
	print >> sys.stderr, pairs, opposed, ip
	for x in ip:
		last = get_prev (op)
		op.append (x)
		if last:
			repl = get_pairs (x, last, pairs)
			if repl:
				op = substitute_op (op, repl)
				x = repl
		if check_for_opposeds (x, op, opposed):
			op = []
	return str (op).replace ("'", "")

def main ():
	r = open ("magika_in")
	w = open ("magika_out", "w+")
	r.readline ()
	cnt = 0
	for ip in r.readlines ():
		cnt += 1
		w.write ("Case #%d: %s\n" %(cnt, str (solve (ip))))
	w.close ()
	r.close ()

main ()
