import sys

t = int(sys.stdin.readline())
cases = []

for i in range(t):
	s = sys.stdin.readline()
	cases.append(s)

for i in range(t):
	tmp = cases[i].split()	
	stand = int(tmp[1][0])
	need = 0
	total_need = need
	for j in range(1, int(tmp[0])+1):
		
		if stand >= j:
			
			stand += int(tmp[1][j])
			
		else:
			need = j - stand
			total_need += need
			stand = stand + int(tmp[1][j]) + need
			
	sys.stdout.writelines("Case #"+str(i+1)+": "+str(total_need)+"\n")
	


