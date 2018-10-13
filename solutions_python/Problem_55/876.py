import sys

def main():
	f = open('C-small.in','r')
	NumCases=int(f.readline())
	#print NumCases
	for i in range (1,NumCases+1):
		R,k,N = f.readline()[:-1].split(' ')
		G = f.readline()[:-1].split(' ')
		g=[]
		Sumg=0
		for n in G:
			g.append(int(n))
			Sumg += int(n)
		#print "Case #%s:" % i 
		#print R,k,N
		#print g, Sumg
		SumEuro = 0
		if Sumg <= int(k):
			SumEuro = Sumg * int(R)
		else:		
			for j in range(1,int(R)+1):
				SumP = 0
				Continue = 0
				while SumP <= int(k) and Continue == 0:
					#GC Group Count
					GC = g.pop(0)
					if SumP + GC <= int(k) and len(g)!= 0:
						SumP += GC
						g.append(GC)
					elif SumP + GC <= int(k) and len(g) == 0:
						SumP += GC	
						Continue = 1
						g.apppend(GC)	
					else:
						g.insert(0,GC)
						Continue = 1
				#print j,SumP,g
				SumEuro += SumP
		print "Case #%s: %s" % (i,SumEuro)				

if __name__ == '__main__': main()	
