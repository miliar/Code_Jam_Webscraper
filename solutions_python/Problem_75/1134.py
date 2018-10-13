#!/usr/bin/env python
import sys
import os

def main():
	n = int(sys.stdin.readline()[:-1])
	c = Pr_B()
	for i in range(1, n+1):
		c.run(i)

class Pr_B:
	#debugflag = True
	debugflag = False
	
	def debug(self, args):
		if(self.debugflag == True):
			print args

	def run(self, case):
		text = sys.stdin.readline()[:-1].split()
		i = 0
		c = None
		ct = None
		d = None
		n = 0
		if int(text[i]) == 1:
			cc = list(text[i+1])
			c = [cc[0],cc[1]]
			ct = cc[2]
			i += 1
		i += 1
		if int(text[i]) == 1:
			dd = list(text[i+1])
			d = [dd[0], dd[1]]
			i += 1
		i += 1
		n = int(text[i])
		i += 1
		invoke = list(text[i])
		self.debug('%d c=%s cc=%s d=%s n=%s invoke=%s' % (case, c, ct, d, n, invoke))
		
		elemlist = []
		for e in invoke:
			self.debug('+++ before %s' % (elemlist,))
			elemlist.append(e)
			self.debug('--- added %s' % (e,))
			self.debug('+++ now %s' % (elemlist,))
			combined = False
			if (c != None and len(elemlist) > 1):
# combine?
				if (c[0] == elemlist[-1] and c[1] == elemlist[-2]) or (c[0] == elemlist[-2] and c[1] == elemlist[-1]):
					combined = True
					self.debug('%d deleting %s %s adding %s' % (case, elemlist[-1], elemlist[-2], ct))
					del elemlist[-1]
					del elemlist[-1]
					elemlist.append(ct)
			if (d != None and combined == False):
				self.debug(elemlist[-1])
				if elemlist[-1] == d[0]:
					self.debug('=== %s found, find %s in %s' % (d[0], d[1], elemlist[:-1]))
					for f in elemlist[:-1]:
						if f == d[1]:
							self.debug('%d found %s and %s, clearing' % (case, d[0], d[1]))
							elemlist = []
							break
				elif elemlist[-1] == d[1]:
					self.debug('=== %s found, find %s in %s' % (d[1], d[0], elemlist[:-1]))
					for f in elemlist[:-1]:
						self.debug('=== %s cmp %s' % (d[0], f))
						if f == d[0]:
							self.debug('%d found %s and %s, clearing' % (case, d[0], d[1]))
							elemlist = []
							break

			self.debug('+++ after %s' % (elemlist,))

		output = str(elemlist)
		output = output.replace("'", "")
		print "Case #%d: %s" % (case, output)

if __name__ == '__main__':
	main()
