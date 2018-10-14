import math

def main(x):
  x=x.split(' ')
  flag=0
  count=0
  c=float(x[0])
  r=float(x[1])
  x1=float(x[2])
  t=[]
  t1=0
  
  total=0

  while count<=math.ceil(x1/c):
      t.append((x1/(2 + (r*count)))+t1)
      t1+=c/(2+((count)*r))
      count+=1
  return "%.7f" %(min(t))

  
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
	