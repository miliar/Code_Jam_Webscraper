#!/usr/bin/env python

# Code for Google Code Jam 2011
# (c) 2011 InterestinglyThere <http://interestinglythere.com/>

## IOLib 1.0.3.0 ##
import os
class iolib:
	defaultenc = None

	def decode(self, s, enc):
		if not enc: return s
		if type(s) == unicode: return s
		elif type(s) == str:
			try: return s.decode(enc)
			except UnicodeDecodeError: return self.progressivedecode(s,enc)
		elif s == None: return
		else: raise TypeError('Must be string or Unicode.')
	def progressivedecode(self, s, enc):
		if not enc: return s
		u = u''
		for c in s:
			try: u += c.decode(enc)
			except UnicodeDecodeError: u += u'?'
		return u
	def encode(self, s, enc=defaultenc):
		if not enc: return s
		if type(s) == str: return s
		elif type(s) == unicode: return s.encode(enc)
		elif s == None: return
		else: raise TypeError('Must be string or Unicode.')

	def read(self, filepath, enc=defaultenc):
		fr = open(filepath, 'r')
		try: content = fr.read()
		except: fr.close();	raise
		decodedcontent = self.decode(content,enc)
		fr.close()
		return decodedcontent
	def write(self, filepath, content, enc=defaultenc):
		fw = open(filepath, 'w')
		encodedcontent = self.encode(content,enc)
		try: fw.write(encodedcontent)
		except: fw.close(); raise
		fw.close()

	def append(self, filepath, content, enc=defaultenc):
		fa = open(filepath, 'a')
		encodedcontent = self.encode(content,enc)
		fa.write(encodedcontent)
		fa.close()
	def touch(self, filepath): return append(filepath, '', enc)

io = iolib()
## / IOBlock ##

def getlines(content, tofind, check=lambda la,le: la==le):
	lines = content.strip().split(tofind)
	numlines = int(lines.pop(0).strip())
	if not check(len(lines),numlines):
		raise RuntimeError('Input said %s lines, but program got %s lines.'%(numlines,len(lines)))
	return numlines, lines

print

# - - - - - - - - - - - - - - - - - -

os.chdir(os.path.expanduser('~/Desktop/GCJ/'))
os.chdir('qual/a/')

# - - - - - - - - - - - - - - - - - -


class DirectivesList:
	def __init__(self, case):
		self.steps = 0
		self.len, self.l = getlines(case, ' ', check=lambda la,le:la==2*le)
		self.queuedPush = False
		self.reset()

	def reset(self): self.remain = self.l[:]

	def incSteps(self): self.steps += 1
	def getSteps(self): return self.steps
	
	def directivesLeft(self):
		return len(self.remain) / 2
	
	def next(self):
		robot = self.remain.pop(0); rawindex = self.remain.pop(0)
		p = int(rawindex.strip())
		if robot == 'O': r = ro
		elif robot == 'B': r = rb
		return r, p

	def addNext(self):
		if not self.directivesLeft(): return False
		r, p = self.next()
		r.rlist += [p]

	def queuePushNext(self): self.queuedPush = True

	def pushNext(self):
		if self.queuedPush:
			self.queuedPush = False
			if not self.directivesLeft(): return False
			if ro.pushTarget==None and rb.pushTarget==None:
				r, p = self.next()
				r.pushTarget = p
	
class Robot:
	def __init__(self, name=None):
		self.i = 1
		self.name = name
		self.rlist = []
		self.info = ''
		self.pushTarget = None

	def getTarget(self):
		if self.rlist: return self.rlist[0]
		else: return None

	def done(self): return not self.rlist

	def left(self):
		self.i-=1
		self.info += '%s: %s <      (%s)'%(
				self.name, tfill(self.i), tfill(self.getTarget()))
	def right(self):
		self.i+=1
		self.info += '%s: %s >      (%s)'%(
				self.name, tfill(self.i), tfill(self.getTarget()))
	def push(self):
		if (self.pushTarget != self.i) and self.getTarget()!=None:
			self.nothing(); return
		self.info += '%s: %s *'%(self.name, tfill(self.i))
		self.pushTarget = None; dlist.queuePushNext()
		if not len(self.rlist): return False
		self.rlist.pop(0)
		return True

	def nothing(self):
		self.info += '%s: %s'%(self.name, tfill(self.i))

	def stay(self):
		self.nothing()
		return False
	
	def move(self):
		if self.i > self.getTarget(): return self.left()
		elif self.i < self.getTarget(): return self.right()
		else: return self.push()

	def act(self):
		self.info = ''
		if self.done(): return self.stay()
		elif self.move() == False: return False
		return True


def cfill(n,l,s):
	n = str(n)
	if l > len(n): return s*(l-len(n)) + n
	else: return n
def rfill(n,l,s):
	n = str(n)
	if l > len(n): return n + s*(l-len(n))
	else: return n
def tfill(n): return cfill(n,3,' ')

# - - - - - - - - - - - - - - - - - -

debug = False

content = io.read('A-large.in.txt')
numcases, cases = getlines(content, '\n')
casenum = 1
for case in cases:
	if debug: print '\nCase #%s steps:'%casenum
	else: print 'Case #%s:'%casenum,

	dlist = DirectivesList(case)
	ro = Robot('O'); rb = Robot('B'); 
	oActed = bActed = True
	
	done = False
	while not done: done = dlist.addNext()==False
	dlist.reset(); dlist.queuePushNext()

	while (oActed or bActed):
		dlist.incSteps()
		dlist.pushNext()

		oActed = ro.act()
		if debug: print rfill('%s: %s'%(tfill(dlist.getSteps()), ro.info),35,' '),

		bActed = rb.act()
		if debug: print '%s'%rb.info

	print dlist.getSteps() - 1
	casenum += 1
