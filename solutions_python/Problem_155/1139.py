'''
Created on Apr 11, 2015

@author: Ankur Patil
'''
import sys
def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		for t in range(1,T+1):
			ans = 0
			tokens = f.readline().split()
			N = int(tokens[0])
			aud = tokens[1]
			standing = 0
			for i in range(N+1):
				if int(aud[i]) != 0 and i > standing:
					ans =  ans + i - standing
					standing = i
				standing = standing + int(aud[i])
				if standing >= N:
					break
			sol.append("Case #{0}: {1}\n".format(t,ans))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])