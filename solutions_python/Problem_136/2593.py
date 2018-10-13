
stdin = open("C:/Users/SAAD/Downloads/B-large.in")
# stdin = open("C:/Users/SAAD/Desktop/codejam14/inn.txt")

T = int(stdin.readline())

for t in range(T):
	C, F, X = (float(e) for e in stdin.readline().split())
	tab = [0]
	V = 2
	ipr = 0
	boo = True
	while boo:
		tab.append(C/V + tab[ipr])
		a=tab[ipr] + X/V
		V += F
		ipr += 1
		b=tab[ipr] + X/(V)
		boo = a>b

	print("Case #"+str(t+1)+": "+str(a))