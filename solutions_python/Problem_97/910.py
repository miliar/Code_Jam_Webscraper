import sys

def sol():
 fin = open('C-small-attempt0.in','r')
 fout = open('C-small.out','w')
 t = int(fin.readline());
 for i in range(t):
  strs = fin.readline().replace('\n',"").split(" ")	
  n = int(strs[0])
  m = int(strs[1])
  count = 0
  j = n 
  for j in range(n,m+1):
	lj = str(j)
	for k in range(1,len(lj)):
		tst = lj[k:]+lj[:k]
		ntst = int(tst)		
		if ntst in range(j+1,m+1): 
			count = count + 1				
  pre = "Case #%d: %d\n"%(i+1,count)
  fout.write(pre)
 fout.flush()
  