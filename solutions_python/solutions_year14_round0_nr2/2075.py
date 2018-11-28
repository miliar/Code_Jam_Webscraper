import sys

def solve(fname1,fname2):
	fin = open(fname1,'r')
	fout = open(fname2,'w')
	T = int(fin.readline())
	for t in range(0,T):
		fout.write("Case #%d: "%(t+1))

		tokens = fin.readline().split()
		tokens = [float(itm) for itm in tokens]
		C = tokens[0]
		F = tokens[1]
		X = tokens[2]
		rate = 2.0
		q = []
		time=0
		while rate*(C/rate+C/F)<X:
			time = time + C/rate
			rate = rate + F
		time = time+X/rate
		fout.write("%.7f\n"%time)		
				
	fin.close()
	fout.close()


if __name__=="__main__":
	fin = sys.argv[1]
	fout = sys.argv[2]
	solve(fin,fout)
