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

def checklen(x, count, check=lambda la,le: la==le):
	if not check(len(x),count):
		raise RuntimeError('Input said %s elements, but program got %s elements.'%(count,len(x)))

def getlines(content, tofind, check=lambda la,le: la==le):
	lines = content.strip().split(tofind)
	numlines = int(lines.pop(0).strip())
	checklen(lines, numlines, check)
	return numlines, lines

def getlines2(content, count, tofind, check=lambda la,le: la==le):
	lines = split(content.strip(), (tofind))
	checklen(lines, count, check)
	return lines

def split(x, sep):
	if len(x) == 0: return []
	else: return x.split(sep)

def sint(x): return int(x.strip()) # 'sint' = strip, then int (:

print

# - - - - - - - - - - - - - - - - - -

os.chdir(os.path.expanduser('~/Desktop/GCJ/'))
os.chdir('qual/b/')

# - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - -

debug = False

import re

content = io.read('B-large.in.txt')

numcases, cases = getlines(content, '\n')
casenum = 1
for case in cases:
	if debug: print '\nCase #%s:'%casenum
	else: print 'Case #%s:'%casenum,

	line = re.split('(\d+ )', case)

	nonbases = getlines2(line[2], sint(line[1]), ' ')
	if debug: print 'nonbases: '+', '.join(nonbases)
	opposings = getlines2(line[4], sint(line[3]), ' ')
	if debug: print 'opposings: '+', '.join(opposings)
	checklen(line[6], sint(line[5]))
	elements = line[6]
	if debug: print 'elements: '+elements

	newElements = ''

	for i in xrange(len(elements)):
		newElements += elements[i]
		
		if len(newElements) >= 2:

			while True:
				for nonbase in nonbases:
					if (newElements.endswith(nonbase[0]+nonbase[1]) or newElements.endswith(nonbase[1]+nonbase[0])):
						newElements = newElements[:-2] + nonbase[2]; break
				else: break

			for opposing in opposings:
				if (opposing[0] in newElements) and (opposing[1] in newElements): 
					newElements = ''

		if debug: print newElements

	if not debug: print '[' + ', '.join(list(newElements)) + ']'

	casenum += 1
