
def main():
	fin = open('D-small-attempt2.in', 'r')#StandingOvationS.in
	fout = open('D.out ', 'w')#StandingOvationS.out
	info = fin.read().splitlines()
	reps = int(info[0])
	for n in range(reps):
		dist = info[n+1].split()
		X = int(dist[0])
		R = int(dist[1])
		C = int(dist[2])
		if n == 3: print(X); print(R); print(C)
		if X == 1:
			fout.write("Case #"+str(n+1)+": GABRIEL\n");
		elif X == 2 and (R*C)%X == 0:
			fout.write("Case #"+str(n+1)+": GABRIEL\n");
		elif X == 4 and (R*C)%X == 0 and R >=3 and C >= 3:
			fout.write("Case #"+str(n+1)+": GABRIEL\n");
		elif X == 3 and (R*C)%X == 0 and R > 1 and C > 1:
			fout.write("Case #"+str(n+1)+": GABRIEL\n");
		else:
			fout.write("Case #"+str(n+1)+": RICHARD\n");

main()