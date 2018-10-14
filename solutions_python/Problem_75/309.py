

import sys
import re

stderr = sys.stderr
def printe(s):
	stderr.write(str(s)+'\n')
	pass

class Magicka(object):
	dd = None
	def __init__(self, line):
		c  = int(line[0])
		self.cc = {i[0:2]: i[2] for i in line[1:c+1]}
		self.cc.update({(i[1]+i[0]): i[2] for i in line[1:c+1]})
		printe(self.cc)
		d  = int(line[c+1])
		v1 = [(i[0]+'.*'+i[1]) for i in line[c+2:]]
		v2 = [(i[1]+'.*'+i[0]) for i in line[c+2:]]
		if v1:
			r1 = '(' + '|'.join(v1+v2) + ')'
			#self.dd = {i[0]: i[1] for i in line[c+2:]}
			self.dd = re.compile(r1)
			printe(r1)
		self.s = ''
	def combine(self):
		if self.s[-2:] in self.cc:
			self.s = self.s[:-2] + self.cc[self.s[-2:]]
			self.combine()
	def opposed(self):
		if self.dd and self.dd.search(self.s):
			self.s = ''
	def invoke(self, c):
		self.s += c
		self.combine()
		self.opposed()
		printe(" s="+self.s)
	def result(self):
		return self.s

inp = sys.stdin
npr = int(inp.readline())
for ip in range(1, npr+1):
	line = inp.readline().split(' ')
	printe('line: '+str(line))
	inv = line[-1].strip()
	m = Magicka(line[:-2])
	for c in inv:
		m.invoke(c)
	print('Case #%d: [%s]'%(ip, ', '.join(m.result())))

