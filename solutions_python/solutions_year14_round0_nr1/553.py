def main(x):
  flag=0
  r=''
  c1=[['','','',''],['','','',''],['','','',''],['','','','']]
  c2=[['','','',''],['','','',''],['','','',''],['','','','']]
  for i in xrange(4):
    c1[i]=inpf.readline().split(' ')
  y=inpf.readline()
  for j in xrange(4):
    c2[j]=inpf.readline().split(' ')
  for m in xrange(4):
    for n in xrange(4):
      if int(c1[int(x)-1][m])==int(c2[int(y)-1][n]):
	flag+=1
	r=str(int(c1[int(x)-1][m]))
  #outp.write("%s" %str(int(c2[0][3])))
  if flag==1:
    return r
  elif flag>1:
    return 'Bad magician!'
  elif flag==0:
    return 'Volunteer cheated!'
  
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
	