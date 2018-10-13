def main(x):
  y=x.split(' ')
  a=int(y[0])
  b=int(y[1])
  fin=int(y[2])
  count=0
  for i in xrange(a):
    for j in xrange(b):
      if i&j<fin:
	count+=1
  return "%s" %str(count)
  
if __name__ == '__main__':
	import sys
	inpf=open('1.txt')
	outp=open('output.txt','w')
	N = int(inpf.readline())
	for i in xrange(N):
		inp=inpf.readline().strip()
		res = main(inp)
		outp.write("Case #%d: %s\n" % (i + 1, res))
	outp.close()
	