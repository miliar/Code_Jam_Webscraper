import sys

def dbg(s): sys.stderr.write(str(s))
def dbgn(s): dbg(str(s) + "\n")

def read(t): return t(raw_input())
def reads(t): return map(t, raw_input().split(" "))



gl = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	]
	
tr = [ "our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	]

trs = {}

trs['z']= 'q'
trs['q']= 'z'

for i in xrange(0,3):
	for j in xrange(0, len(gl[i])):
		trs[gl[i][j]] = tr[i][j]


T = read(int)

for t in xrange(1, T+1):
	
	glrs = read(str)
	normal = ""	
	for i in xrange(0, len(glrs)):
		g = glrs[i]
		normal += trs[g]
	
	print "Case #%d: %s" % (t, normal)
