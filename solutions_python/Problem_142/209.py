# REASON NUMBER TWO WHY CIVILIZATIONS DIE:
# MANY SOFTWARE ENGINEERS ARE TRAINED TO
# IMPLEMENT AND SUBMIT SOLUTIONS WITHIN 2.5
# HOURS, BELIEVING THE SOLUTIONS ARE BUG-FREE

import sys
inp = sys.stdin
T = int(inp.readline())

def readbins():
	return [int('0b'+x,2) for x in raw_input().strip().split()]
def readints():
	return [int(x) for x in raw_input().strip().split()]
def readstrs():
	return [str(x) for x in raw_input().strip().split()]
def readfloats():
	return [float(x) for x in raw_input().strip().split()]
def countbits(x):
	res=0
	while x:
		res+=x&1
		x>>=1
	return res

for t in range(1, T+1):
  print 'Case #'+str(t)+':',
  N = int(inp.readline())
  strs = [""]*N
  for i in range(N): strs[i] = inp.readline().strip()
  minlen = 555
  maxlen = 0
  equal = 1
  nowin = 0
  s0 = strs[0]
  l0 = len(s0)
  for s in strs:
	l = len(s)
	#if l<minlen: minlen=l
	#if l>maxlen: maxlen=l
	if strs[0]!=s: equal=0
	if s[0]!=s0[0] or s[l-1]!=s0[l0-1]: nowin=1
  if equal==1:
	print 0
	continue
  if nowin==1:
	print 'Fegla Won'
	continue

  res=0
  nowin = 0
  while 1:
	ns = []
	for s in strs:
		if len(s)==0 or s[0]!=strs[0][0]:
			nowin=1
			break
		n = 0
		for c in s:
			if c==s[0]: n+=1
			else:		break
		ns.append(n)

	if nowin==1: break

	nss = sorted(ns)
	partsum = [0]*N
	sum = 0
	for i in range(N):
		sum += nss[i]
		partsum[i] = sum

	minr=77777777
	for i in range(N):
		j = nss[i]
		r = 0
		if i!=0:
			r += j*i - partsum[i-1]
		if i!=N-1:
			r += partsum[N-1] - partsum[i] - j*(N-1-i)
		if r<minr: minr=r
	res+=minr

	i = sl = 0
	for s in strs:
		strs[i] = s[ns[i]:]
		sl += len(strs[i])
		i+=1
	if sl==0: break

  if nowin==1:
	print 'Fegla Won'
	continue

  print res
