def main(x):
  result='Draw'
  for i in range(0,4):
    if x[i][0]!='.' and x[i][0]!='T':
      flag=x[i][0]
    else:
      continue
    count=0
    for j in range(0,4):
      if x[i][j]==flag or x[i][j]=='T':
	count+=1
      else:
	break
    if count==4:
      result=flag+' won'
  count=0
  for i in range(0,4):
    if x[0][i] != '.' and x[0][i] != 'T':
      flag=x[0][i]
    else:
      continue
    count1=0
    for j in range(0,4):
      if x[j][i]==flag or x[j][i]=='T':
	count1+=1
      else:
	break
    if count1==4:
      result=flag +' won'
  count1=0
  for i in range(0,4):
    if x[0][0] != '.' and x[0][0] != 'T':
      flag=x[0][0]
    else:
      continue
    if flag==x[i][i] or x[i][i]=='T':
      count1+=1
    else:
      break
  if count1==4:
    result=flag +' won'
  if x[0][3] != '.' and x[0][3] != 'T':
    flag=x[0][3]
    if (x[1][2]==flag or x[1][2]=='T') and (x[2][1]==flag or x[2][1]=='T') and (x[3][0]==flag or x[3][0]=='T'):
      result=flag + ' won'
  if result=='Draw':
    for i in range(0,4):
      for j in range(0,4):
	if x[i][j]=='.':
	  result='Game has not completed'
	  break
  return result

if __name__ == '__main__':
	import sys
	inp=[[''],[''],[''],['']]
	inpf=open('1.txt')
	outp=open('output.txt','w')
	N = int(inpf.readline())
	for i in xrange(N):
		for j in xrange(4):
		  inp[j]=inpf.readline().strip()
		res = main(inp)
		K=inpf.readline().strip()
		outp.write("Case #%d: %s\n" % (i + 1, res))
	outp.close()