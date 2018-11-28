import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import itertools
import math

def readstr(f): return f.readline()[:-1]
def readfloat(f): return float(readstr(f))
def readint(f): return int(readstr(f))
def readstrs(f): return readstr(f).split(' ')
def readints(f): return map(int, readstrs(f))
def readfloats(f): return map(float, readstrs(f))

def main():
	fn = raw_input('File name: ')
	f = open(fn)
	o = open('output.txt','w')
	no_cases = readint(f)
	for x in xrange(no_cases):
		para1 = readint(f) #no of lines
		para2 = [tuple(readints(f)) for i in range(para1)]
		para3 = readint(f)
		result = a(para2,para3)
		o.write("Case #"+str(x+1) + ": " + result + '\n')
		logging.debug(str(x+1)+ "/"+ str(no_cases) +"Done")
	f.close()
	o.close()

def a(lines, ttd):
	if ttd == 0 or ttd == lines[0][0]:
		return "YES"
	lines += [(ttd,999)]
	start = (0,lines[0])
	searched = set()
	to_search = [ [start] ]
	logging.debug(to_search)
	while to_search:
		path = to_search.pop(0)
		s = path[-1]
		for (state, action) in successors(s,lines).items():
			if state not in searched:
				searched.add(state)
				path2 = path + [action, state]
				if state[1][0] == ttd:
					return "YES"
				else:
					to_search.append(path2)
	return "NO"


def successors(s , ls):
	at , holding = s
	d = {(holding[0],(pos,l)):'Reach ' + str(pos) for (pos,l) in ls if pos > holding[0] and pos <= min(2*holding[0] - at,holding[0]+holding[1])}
	logging.debug(d)
	return d

main()
