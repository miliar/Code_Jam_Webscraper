import math
import bisect


def isPolidrom(n):
	return str(n) == (str(n)[::-1])
	
getBin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]	

def f(n):
	result = 0
	for i in xrange(int(math.sqrt(n))+1):	
		if isPolidrom(i) and isPolidrom(i*i):
			#print "%d \t\t\t <- %d" % (i*i, i)
			#print i*i
			result += 1
		
	return result

def solve(a,b):
	return f(b) - f(a-1)

def f2(n):
	a = [1,2,3]
	f = open("numbers3.txt","w")
	for pref in xrange(2**n):
		spref = getBin(pref)
		a += [int(spref + spref[::-1])]
		if len(spref) <= 24:
			for middle in range(3):
				a += [int( spref + str(middle) + spref[::-1] )] 
		'''
		if pref%(2**(n-7)) == 0:
			print "prgress %d" % int(pref/(2**(n-7)))
		'''
			
			
	for i in xrange(n):
		spref = "2" 
		for j in xrange(i):
			spref += "0"
		a += [int(spref + spref[::-1])]
		for middle in range(3):
			a += [int( spref + str(middle) + spref[::-1] )] 
		
		
		
	a = sorted(a)
	b = []
	for i in a:
		if isPolidrom(i) and isPolidrom(i*i):
			b += [i*i]
	
	fout = open("output_large1.txt","w");
	with open('C-large-1.in') as f:
		t = int(f.readline())
		for i in xrange(t):
			l, r = [int(x) for x in f.readline().split()]
			#fout.write("Case #%d: %s\n" % (i+1, str(solve(l,r)) ))
			
			aa =  bisect.bisect_left(b,l)
			bb =  bisect.bisect_right(b,r);

			fout.write("Case #%d: %s\n" % (i+1, str(bb-aa) ))
			
	
	'''
	print "|a| = %d" % len(a)
	for i in a:
		if isPolidrom(i) and isPolidrom(i*i):
			#print "%d \t\t\t <- %d" % (i*i, i)
			#print i*i
			f.write( ("%d\n"%(i*i)) )
			
	f.close()		
	'''
			

	
def main():
	fout = open("output.txt","w");
	with open('input.txt') as f:
		t = int(f.readline())
		for i in xrange(t):
			a, b = [int(x) for x in f.readline().split()]
			fout.write("Case #%d: %s\n" % (i+1, str(solve(a,b)) ))
		
if __name__ == '__main__':
	#f(10**14)
	f2(5)
		
