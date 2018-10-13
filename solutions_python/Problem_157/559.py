import fileinput
import functools

def solve(s, repeats):
	s = s[:-1]*repeats
	if not compute(s) == "1-":
		return "NO"
	s = list(s)
	consumed = "1"
	while len(s)>0:
		i = s.pop(0)
		consumed = mult(consumed, i)
		if consumed == "i":
			if len(s) > 0:
				if compute(s) == "i":
					if findjksplit(s):
						return "YES"
	return "NO"

def findjksplit(s):
	consumed = "1"
	while len(s)>0:
		i = s.pop(0)
		consumed = mult(consumed, i)
		if consumed == "j":
			return True
	return False

def compute(s):
	return functools.reduce(mult, s)

def mult(aa, bb):
	a = aa[0]
	b = bb[0]
	r = 0
	if a == "1":
		r = b
	if b == "1":
		r = a
	if a == "i" and b == "i":
		r = "1-"
	elif a == "i" and b == "j":
		r = "k"
	elif a == "i" and b == "k":
		r = "j-"
	elif a == "j" and b == "i":
		r = "k-"
	elif a == "j" and b == "j":
		r = "1-"
	elif a == "j" and b == "k":
		r = "i"
	elif a == "k" and b == "i":
		r = "j"
	elif a == "k" and b == "j":
		r = "i-"
	elif a == "k" and b == "k":
		r = "1-"
	if r == 0:
		print(aa)
		print(bb)
		raise Exception
	if not len(aa) == len(bb):
		if len(r) == 2:
			return r[0]
		if len(r) == 1:
			return r + "-"
	else:
		return r



lines = fileinput.input()
testcases = int(lines.readline())
   
for caseNr in range(1, testcases+1):
    line1 = lines.readline()
    noChars = int(line1.split()[0])
    repeats = int(line1.split()[1])
    s = lines.readline()
    print("Case #%i: %s" % (caseNr, solve(s, repeats)))

