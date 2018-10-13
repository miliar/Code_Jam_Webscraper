import re, sys, math, pdb

def eOiI ():
	print("No valid input given!")
	sys.exit(1)

def strip (s):
	return s.strip()

f = open("input.in")
s = f.readline()
m = re.search('^\s*(\d+)\s*$', s)
if m == None:
	eOiI()
c = int(m.group(1)) + 1
found = {}
for i in range(1,c):
	m = re.search('^\s*(\d+)\s+(\d+)\s*$', f.readline())
	if m:
		a = int(m.group(1))
		b = int(m.group(2))

		if a > b:
			print('Case #{0}: 0'.format(i))
		else:
			count = 0
			d = math.ceil(math.sqrt(a))
			finished = False
			while not finished:
				if d in found:
					if found[d] <= b:
						count += 1
					else:
						finished = True
				elif repr(d)[::-1] == repr(d):
					e = d*d
					if e <= b:
						r = repr(e)
						if r[::-1] == r:
							found[d] = e
							count += 1
					else:
						finished = True
				d += 1
			print('Case #{0}: {1}'.format(i,count))
	else:
		eOiI()

