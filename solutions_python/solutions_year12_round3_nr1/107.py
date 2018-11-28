# Python 2.7.2 (2346207d99463f299f09f3e151c9d5fa9158f71b, Apr 14 2012, 18:57:04)
# [PyPy 1.8.0] on darwin
# (C) 2012 Dennis Bliefernicht

BASENAME="A"
TYPE="ex"
TYPE="sm1"
TYPE="la"
NODOUT=True

seennodes = set()
isdiamond = False

def visit(node, tree):
	global seennodes, isdiamond
	
	dout("Visiting", node, seennodes)
	if isdiamond:
		return
	
	if node in seennodes:
		isdiamond = True
		return
	
	seennodes.add(node)
	childs = tree[node][1]
	
	for c in childs:
		visit(c, tree)
	
def process():
	global seennodes, isdiamond
	
	nclass = popint()
	inh = []
	for x in range(nclass):
		a = popintarray()
		inh.append( (a[0], map(lambda x: x-1, a[1:])) )
	
	# find all nodes that aren't inherited by anyone
	noinh = set()
	for x in range(nclass):
		isinh = False
		for y in range(nclass):
			if x in inh[y][1]:
				isinh = True
				break
		if not isinh:
			noinh.add(x)
			
	dout(inh)
	dout(noinh)
			
	# do a tree search starting form these nodes
	for x in noinh:
		seennodes.clear()
		isdiamond = False
		visit(x, inh)
		
		if isdiamond:
			return "Yes"
#		dout("restart")
#		tovisit = set()
#		seennodes = set()
#		
#		tovisit.add(x)
#		while len(tovisit) > 0:
#			v = tovisit.pop()
#			seennodes.add(v)
#			ch = inh[v][1]
#			
#			for c in ch:
#				if c in seennodes:
#					return "Yes"
#				tovisit.add(c)
			
	return "No"

# ------------------------------------
# GCJ2012 framework stuff
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
	