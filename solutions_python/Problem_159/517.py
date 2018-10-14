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
			ans1 = 0
			ans2 = 0
			N = int(f.readline())
			tokens = f.readline().split()
			m = []
			m.append(int(tokens[0]))
			diff = []
			prev = m[0]
			for i in tokens[1:]:
				m.append(int(i))
				if prev > int(i):
					diff.append(prev-int(i))
				prev = int(i)
			mx = 0
			for i in diff:
				ans1 = ans1 + i
				mx = max(mx,i)
			print(mx)
			for i in m[:-1]:
				ans2 = ans2 + min(mx,i)
			sol.append("Case #{0}: {1} {2}\n".format(t,ans1,ans2))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])