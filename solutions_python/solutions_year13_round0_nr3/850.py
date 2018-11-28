#!/usr/bin/python
import sys

def startPalin():
	return (1,1,True,9) # current, started, width, limit

def nextPalin((cur,st,odd,limit)):
	if cur==limit:
		if odd:
			return (st,st,False,limit)
		else:
			return (cur+1,cur+1,True,limit*10+9)
	else:
		return (cur+1,st,odd,limit)

def palinToNum((cur,st,odd,limit)):
	l = str(cur)
	r = l[::-1]

	if odd:
		r = r[1:]

	return int(l+r)

def sqr(n):
	return n*n


def isPalin(num):
	s = str(num)
	return s==s[::-1]

"""
p = startPalin()
#for i in range(20):
#	p = nextPalin(p)
for i in range(100):
	#print p, palinToNum(p),' '
	print palinToNum(p),' ',
	p = nextPalin(p)
raise "x"
"""

inp = [l.strip() for l in sys.stdin]

T = int(inp[0])
inp2 = [s.split() for s in inp[1:T+1]]
As = [int(l[0]) for l in inp2]
Bs = [int(l[1]) for l in inp2]
results = [0]*T

#print As,Bs

limit = 10**100
limit = 10**14
p = startPalin()
while True:
	sq = sqr(palinToNum(p))
	#if sq>100000000000000:
	if sq>limit:
		break
	if not isPalin(sq):
		p = nextPalin(p)
		continue
	#print "checking ",p,sq
	for t in range(T):
	  	if sq>=As[t] and sq<=Bs[t]:
	  		results[t]+=1
	p = nextPalin(p)

for t in range(T):
	print "Case #%d: %d" % (t+1, results[t])

















"""

l = 1
for t in range(T):
  ab = map(int, inp[t+1].split())

  a = ab[0]
  b = ab[1]
  cnt = 0

  p = startPalin()
  while True:
  	sq = sqr(palinToNum(p))
  	if sq is None:
  		p = nextPalin(p)
  		continue

  	if (isPalin(sq)):
	  	if sq>b:
	  		break;
	  	elif sq>=a:
	  		cnt+=1
	p = nextPalin(p)

  print "Case #%d: %d" % (t+1, cnt)

"""