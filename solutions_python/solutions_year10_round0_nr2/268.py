#BISMILLAHIRRAHMANIRRAHIM

from fractions import gcd





def main():
	T=int(raw_input())+1
	for I in xrange(1,T) :
		l=raw_input().split();
		n=int(l[0])
		g=abs(int(l[1])-int(l[2]))
		for i in xrange(1,n) :
			#print i,g
			g=gcd(g,abs(int(l[i])-int(l[i+1])))
		#print g
		if (int(l[1])%g)==0 : ans = 0
		else : ans = g-(int(l[1])%g)
		print "Case #%d: %d"%(I,ans)
	return 0

if __name__ == '__main__':
	main()
