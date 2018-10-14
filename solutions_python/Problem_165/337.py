def main(x):
  r,c,w=x.split(' ')
  r,c,w=int(r),int(c),int(w)
  result=w+(r*(c/w))-1
  if c%w<>0:
    result+=1
  return result
  
  
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
	