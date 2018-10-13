
stdin = open("C:/Users/SAAD/Downloads/A-small-attempt0.in")

T = int(stdin.readline())

for t in range(T):
	p = int(stdin.readline())
	pg = []
	for l in range(4):
		# print(stdin.readline().split())
		pg.append(set(int(e) for e in stdin.readline().split()))
	pp = int(stdin.readline())
	ppg = []
	for l in range(4):
		ppg.append(set(int(e) for e in stdin.readline().split()))
	inter = list(pg[p-1] & ppg[pp-1])

	l = len(inter)
	if l == 0:
		print("Case #"+str(t+1)+": Volunteer cheated!")
	elif l == 1:
		print("Case #"+str(t+1)+": " + str(inter[0]))
	else :
		print("Case #"+str(t+1)+": Bad magician!")