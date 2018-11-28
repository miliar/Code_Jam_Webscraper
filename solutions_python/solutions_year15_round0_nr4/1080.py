def main(y):
  X=int(y.split(' ')[0])
  R=int(y.split(' ')[1])
  C=int(y.split(' ')[2])
  if X==R and R==C:
    return 'GABRIEL'
  if X==1:
    return 'GABRIEL'
  if R*C%X<>0:
    return 'RICHARD'
  if X>2 and (R==1 or C==1):
    return 'RICHARD'
  if X>R and X>C:
    return 'RICHARD'
  if X==4 and (R==2 or C==2):
    return 'RICHARD'
  if X==4 and (R==3 or C==3):
    return 'GABRIEL'
  if X==3:
    return 'GABRIEL'
  if X==2 and R*C%2==0:
    return 'GABRIEL'

  
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
	