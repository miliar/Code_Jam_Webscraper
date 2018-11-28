#!/usr/bin/python
import sys

def nextLine():
	return sys.stdin.next()[:-1]

def debug(s):
	sys.stderr.write("# "+s+"\n")

def vec(line):
	v = []
	c = [0]*10
	for i in line:
		ii = int(i)	
		v.append(ii)
		c[ii] += 1
	return (v,c)

def build(v,c,next):
	for i in xrange(next+1,len(c)):
		if c[i] > 0:
			v.append(i)
			c[i]-=1
			break
	for i in xrange(len(c)):
		v.extend([i]*c[i])
	return v

def next(obj):
	count = 0
	v0,c0 = obj
	v1,c1 = [],[0]*10
	L = len(v0)
	for p in xrange(L):
		ii = v0.pop()
		v1.append(ii)
		c0[ii] -= 1
		c1[ii] += 1
		count += 1
		if count > 1 and v1[-1] < v1[-2]:
			#lex order
			return build(v0,c1,v1[-1])
	c1[0] +=1
	min = 0
	for i in xrange(1,len(c1)):
		if c1[i] > 0 :
			min = i
			break
	return build(v0,c1,min-1)

		

	
def tostr(v):
	s = ""
	for i in v:
		s += str(i)
	return s

N = int(nextLine())
for c in range(N):
	input = vec(nextLine())
	print "Case #%d: %s"%(c+1,tostr(next(input)))

