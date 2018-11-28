import math

def once(r,t):
	out=(math.sqrt(8*t+4*r*r-4*r+1)-2*r-3)/4
	out=out+1
	print "out={}".format(out)
	rr=round(out)
	if rr>out:
		rr=rr-1
 
#	print "out={} rout={}".format(out, rout)
	
	return int(rr)	

def main():
	f=open("A-small-attempt0.in", 'r')
	f1=open("output.txt", 'w')
	for i in range(int(f.readline())):
		line=f.readline().split()
		r=int(line[0])	
		t=int(line[1])
		
		output=once(r,t) #call once with appropriate arguments
		f1.write("Case #{}: {}\n".format(i+1, output))
		print i

main()
#once(10000000000000000, 1000000000000000000)
#once(2, 13)
