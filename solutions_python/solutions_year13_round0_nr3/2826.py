def main(x):
  lo=int(x.split(' ')[0])
  up=int(x.split(' ')[1])
  count=0
  for i in range(lo, up+1):
    d=str(i)
    c=i**.5
    e=str(int(c))
    if d==d[::-1] and c.is_integer() and e==e[::-1]:
      count+=1
  return count

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
	