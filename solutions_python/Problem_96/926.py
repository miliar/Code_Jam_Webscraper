import sys

def getsup_norm(num):
 sup = 0
 norm = 0
 if(num % 3 == 2):
  norm = ((num-2)/3)+1
  sup = norm+1
 elif(num % 3 == 1):
  norm = ((num-1)/3)+1
  sup = norm
 else:
  norm = num/3
  sup = norm+1
 return sup,norm

def sol():
 fin = open('B-large.in','r')
 fout = open('B-large.out','w')
 n = int(fin.readline());
 for j in range(0,n):
  str = fin.readline().replace('\n',"").split(" ")	
  n = int(str[0])
  s = int(str[1])
  p = int(str[2])
  count = 0
  tsup = []
  tnorm = []
  for i in range(3,len(str)):
	 nu = int(str[i])
	 if nu == 0:
	  tsup.append(0)
 	  tnorm.append(0)
	 elif nu == 1:
	  tsup.append(1)
 	  tnorm.append(1)
	 else:
	  sup,norm = getsup_norm(nu)
	  tsup.append(sup)
 	  tnorm.append(norm) 
  for su in range(len(tsup)):
	 if s == 0:
	  break
	 if (tsup[su] >= p) and (tnorm[su] < p):
	  s = s-1
	  count=count+1
	  tsup[su] = -1
	  tnorm[su] = -1
  if s != 0:
  	for l in range(len(tsup)):
	 if s == 0:
	  break 
	 if tsup[l] >= p:
	  s = s-1
	  count=count+1
	  tsup[l] = -1
	  tnorm[l] = -1
  for k in range(len(tsup)):
	if tnorm[k] >= p:
	 count = count+1
  pre = "Case #%d: %d" %(j+1,count)
  fout.write(pre+'\n')
 fout.flush()
  