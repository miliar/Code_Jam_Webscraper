import sys
import re

def getLine():
	global fin
	line = fin.readline()
	if line[-1]=="\n":
		line = line[:-1]
	return line


def solve():
	T = int(getLine())
	m = re.match(r"(\d+) (\d+)$",getLine())
	na = int(m.group(1))
	nb = int(m.group(2))
	print T,na,nb
	table = []
	for i in xrange(na+nb):
		m = re.match("(\d\d):(\d\d) (\d\d):(\d\d)",getLine())
		h1,m1,h2,m2 = map(int,m.groups())
		table.append((h1*60+m1,h2*60+m2))
	a = table[:na]
	b = table[na:]

	events = []
	for i in a:
		events.append((i[0],-1,0))
		events.append((i[1]+T,0,+1))
	for i in b:
		events.append((i[0],0,-1))
		events.append((i[1]+T,+1,0))

   	events.sort()
  	events.append((86400,0,0))
   	state = (0,0,0)
   	minA = 0
   	minB = 0
   	for e in events:
#   		print state
   		if e[0]>state[0]:
   			minA = max(minA,-state[1])
   			minB = max(minB,-state[2])
   		state = e[0],state[1]+e[1],state[2]+e[2]
#	print a,b
	return "%s %s"%(minA,minB)

#########
if len(sys.argv) != 2:
	print "Specify input file"
	exit(1)

fin = open(sys.argv[1])


n = int(getLine())

fout = open("out","wt")

for i in range(n):
	print "Solving",i
	fout.write("Case #%s: "%(i+1))
	fout.write(solve())
	fout.write("\n")

fout.close()