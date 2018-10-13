import sys
import math


def read(filename):
	f=open(filename,'r')
	lines=f.readlines()
	
	lines[-1]=lines[-1]+'\n'
#	print lines

	
	newlines=[]
	words=[]
	for i in lines:
		words=i.split(" ")	
		
		words[-1]=words[-1][:-1]
		#print words	
		newlines.append(words)
	return newlines	

def palin_check(n):
	s=str(n)
	s2=s[::-1]
	if s==s2:
		return 1
	else:
		 return 0
	


def solve(block):
	xa=block[0]
	xb=block[1]
	a=math.sqrt(int(xa))
	b=math.sqrt(int(xb))
	
	a2=math.floor(a)
	b2=math.floor(b)

	if(a-a2==0.0):
		a=a

	else :
		a=math.floor(a)+1

	if(b-b2==0.0):
		b=b
	else:
		b=math.floor(b)

#	print a,b

	count=0
	for i in range(int(a),int(b)+1):
		if(( palin_check(i) == 1) and (palin_check(i*i) == 1 ) ):
#			print i, i*i
			count=count+1

	return count

	


def main():
   c=read(sys.argv[1])
   size=c[0][0]
   
   for i in range(1,len(c)):
	opnum=solve(c[i])
	print "Case #"+str(i)+": "+str(opnum)
 
   
#   print (palin_check(1442441))
   
if __name__=="__main__":
    main()
   
