# /usr/bin/python
import sys

def dbg(s): sys.stderr.write(str(s) +"\n")
def reads(t): return map(t, input().split(" "))
def readstrtolist(): return [x  for x in input()]
def read(t) : return t(input())

def line():
	return ['z', 0]

def add_symb(line, symb):
	[s, cnt] = line
	#~ dbg("before: " + str(line))
	if symb == '.':
		pass
	elif symb == s or symb == 'T' or s == 'T':
		line[1] = cnt + 1
		if s == 'T':
			line[0] = symb
		
	elif s == 'z':
		line[0] = symb
		line[1] = 1
		
	else:
		line[0] = 'b'
		line[1] = -4
		
	#~ dbg("after: " + str(line))
	
	return line


T = read(int)

for t in range(1, T+1):
	cols = [line(), line(), line(), line()]
	rows = [line(), line(), line(), line()]
	d1 = line()
	d2= line()
	
	dot = False;
	
	for i in range(0, 4):
		row = input()
		#~ dbg(row)
		for j in range(0,4):
			symb = row[j]
			if symb == '.':
				dot = True
			#~ dbg("%d, %d" % (i,j))
			#~ dbg("row")
			add_symb(rows[i], symb)
			#~ dbg("col")
			add_symb(cols[j], symb)
			if i == j:
				#~ dbg("d1")
				add_symb(d1, symb)
			if i == 3 - j:
				#~ dbg("d2")
				add_symb(d2, symb)
	
	all_lines = cols + rows + [d1, d2]
	all_lines = sorted(all_lines, key=lambda l: l[1])
	
	#~ dbg(all_lines)
	
	maybe_won = all_lines[9]
	
	cnt = maybe_won[1]
	if cnt == 4:
		s = maybe_won[0]
		print("Case #%d: %s won" % (t, s))
	elif dot:
		print("Case #%d: Game has not completed" % (t))
	else:
		print("Case #%d: Draw" % (t))
		
	input()
