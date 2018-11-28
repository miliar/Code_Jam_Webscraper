def find(A,B,K):
	count = 0
	for a in range(A):
		for b in range(B):
			if (a&b) < K:
				count +=1
	return count

def main():
	fin = open('B-small-attempt0.in')
	fout = open('out.txt', 'w')

	cases = int(fin.readline())

	for case in range(cases):
		print case
		line = fin.readline().split()
		ans = find(int(line[0]), int(line[1]), int(line[2]))
		fout.write("Case #"+str(case+1)+ ": "+str(ans) +"\n")



	fin.close()
	fout.close()



main()



