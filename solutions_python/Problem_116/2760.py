import sys


def read(filename):
	f=open(filename,'r')
	lines=f.readlines()
	newlines=[]
	words=[]
	for i in lines:
		words=i.split(" ")	
		words[-1]=words[-1][:-1]
		#print words	
		newlines.append(words)
	return newlines	

##################################################################

def arrange(d):
	block=[]
	blockset=[]
	for i in range(1,len(d)):
		if (i%5 == 0) and len(block)!=0 :
			blockset.append(block)
			block=[]
		else :
			block.append(d[i])
	return blockset
	
def solve(block):
	p=block[0]
	q=block[1]
	r=block[2]
	s=block[3]
	

	e=['X','T']
	if(
		(p[0][0] in e and p[0][1] in e and p[0][2] in e and p[0][3] in e)
	or    
		(q[0][0] in e and q[0][1] in e and q[0][2] in e and q[0][3] in e)
	or	
		(r[0][0] in e and r[0][1] in e and r[0][2] in e and r[0][3] in e)
	or	
		(s[0][0] in e and s[0][1] in e and s[0][2] in e and s[0][3] in e)
	
	or	
		(p[0][0] in e and q[0][0] in e and r[0][0] in e and s[0][0] in e)
	or	
		(p[0][1] in e and q[0][1] in e and r[0][1] in e and s[0][1] in e)
	or	
		(p[0][2] in e and q[0][2] in e and r[0][2] in e and s[0][2] in e)
	or	
		(p[0][3] in e and q[0][3] in e and r[0][3] in e and s[0][3] in e)
	
	or	
		(p[0][0] in e and q[0][1] in e and r[0][2] in e and s[0][3] in e)
	or	
		(p[0][3] in e and q[0][2] in e and r[0][1] in e and s[0][0] in e)
	):
	  return "X won"
	
	e=['O','T']
	if(
		(p[0][0] in e and p[0][1] in e and p[0][2] in e and p[0][3] in e)
	or    
		(q[0][0] in e and q[0][1] in e and q[0][2] in e and q[0][3] in e)
	or	
		(r[0][0] in e and r[0][1] in e and r[0][2] in e and r[0][3] in e)
	or	
		(s[0][0] in e and s[0][1] in e and s[0][2] in e and s[0][3] in e)
	
	or	
		(p[0][0] in e and q[0][0] in e and r[0][0] in e and s[0][0] in e)
	or	
		(p[0][1] in e and q[0][1] in e and r[0][1] in e and s[0][1] in e)
	or	
		(p[0][2] in e and q[0][2] in e and r[0][2] in e and s[0][2] in e)
	or	
		(p[0][3] in e and q[0][3] in e and r[0][3] in e and s[0][3] in e)
	
	or	
		(p[0][0] in e and q[0][1] in e and r[0][2] in e and s[0][3] in e)
	or	
		(p[0][3] in e and q[0][2] in e and r[0][1] in e and s[0][0] in e)
	):
	  return "O won"
	
	for i in range(3):
	  for j in range(3):
	    if ( (p[0][j] == '.') or (q[0][j] == '.') or (r[0][j] == '.') or (s[0][j] == '.') ):
	      return "Game has not completed"
	
	return "Draw"
	
	
	
	
def main():
  lines=read(sys.argv[1])
  size = int(lines[0][0])
  newlines = arrange(lines)

  for i in range(size):
	opstring=solve(newlines[i])
	print "Case #"+str(i+1)+': '+opstring
	
	

if __name__=="__main__":
	main()
