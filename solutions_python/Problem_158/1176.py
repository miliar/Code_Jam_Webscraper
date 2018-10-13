#Ominous Ominos

infile = open('bla.txt','r')
infile = infile.readlines()
ans = []
T = int(infile[0])
cont = False
def factor(number):
	a = []
	for i in range(1,number+1):
		a.append((i,number-i))
	return a
for case in range(1,T+1):
	string = infile[case]
	x = int(string.split()[0])
	r = int(string.split()[1])
	c = int(string.split()[2])
	list = factor(x)
	for tuple in list:
		a = tuple[0]
		b = tuple[1]
		if a > r or b > r or a > c or b > c:
			ans.append("Case #" + str(case) + ": RICHARD")
			cont = True
			break
		elif r*c % x != 0:
			ans.append("Case #" + str(case) + ": RICHARD")
			cont = True
			break
		elif x == r and x == c:
			ans.append("Case #" + str(case) + ": GABRIEL")
			cont = True
			break
		else:
			ans.append("Case #" + str(case) + ": GABRIEL")
			cont = True
			break
	if cont:
		continue	

for i in ans:
	print(i)