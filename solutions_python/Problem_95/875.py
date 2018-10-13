#!/usr/bin/python
'''
Google codejam template
'''
import sys, re
#fh = sys.stdin
fh = open(sys.argv[1])
cases = int(fh.readline())

code = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''

english = '''
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
'''
english = re.sub('Case #\d: ', '', english)
code = re.sub('[\n\t]', '', code)
english = re.sub('[\n\t]', '', english)
assert re.search('^[a-z ]+$', code)
assert re.search('^[a-z ]+$', english)
assert len(code) == len(english)

mapping = { # to decode
	'y': 'a',
	'e': 'o',
	'q': 'z',
	}

for e, c in zip(english, code):
	if c in mapping:
		mapping[c] == e
	else:
		mapping[c] = e

mc = None # missing code
me = None # missing english
for i in range(ord('a'), ord('z')+1):
	c = chr(i)
	if c not in mapping:
		assert not mc
		mc = c
	if c not in mapping.values():
		me = c
mapping[mc] = me

for case in range(1, cases+1):
	print 'Case #%i:' % case,
	line = fh.readline().rstrip('\n\r')
	print ''.join([mapping[i] for i in line])
