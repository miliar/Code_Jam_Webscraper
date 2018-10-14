def construct(r,b,y):
	D = {"R": r, "B": b, "Y": y}
	d = {"R": r, "B": b, "Y": y}
	answer = ""
	while sum(d.values()) > 0:
		k = sorted(d.keys(), key=lambda x: (d[x],D[x]), reverse=True)
		if not answer or answer[-1] != k[0]:
			answer += k[0]
			d[k[0]] -= 1
		else:
			answer += k[1]
			d[k[1]] -= 1
	return answer

def find(s, c):
	i = 0
	while s[i] != c:
		i+=1
	return i

def add(answer, g,o,v):
	if g > 0:
		i = find(answer,"R")
		answer = answer[:i] + "RG"*g + answer[i:]
	if o > 0:
		i = find(answer,"B")
		answer = answer[:i] + "BO"*o + answer[i:]
	if v > 0:
		i = find(answer,"Y")
		answer = answer[:i] + "VY"*v + answer[i:]
	return answer

T = int(raw_input())
impossible = "IMPOSSIBLE"
for test_case in range(T):
	N,R,O,Y,G,B,V = [int(x) for x in raw_input().split()]
	if any([G**2>R**2,O**2>B**2,V**2>Y**2]):
		if O+B+V+Y == 0 and G==R:
			answer = "RG"*G
		elif G+R+V+Y == 0 and O==B:
			answer = "OB"*O
		elif G+R+O+B == 0 and V==Y:
			answer = "VY"*V
		else:
			answer = impossible
			assert False, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(N,R,O,Y,G,B,V,G**2>=R**2,O**2>=B**2,V**2>=Y**2)
	else:
		r,b,y = R-G,B-O,Y-V
		n = r+b+y
		if any([r>n/2,b>n/2,y>n/2]):
			answer = impossible
		else:
			answer = construct(r,b,y)
			answer = add(answer,G,O,V)
			assert R == answer.count("R")
			assert Y == answer.count("Y")
			assert B == answer.count("B")
			assert G == answer.count("G")
			assert O == answer.count("O")
			assert V == answer.count("V")
			wrapped = answer + answer[0]
			for s in ["RR", "YY", "BB", "GG", "OO", "VV"]:
				assert wrapped.count(s) == 0, wrapped
			for s in ["GY", "GB", "YG", "BG"]:
				assert wrapped.count(s) == 0, wrapped
			for s in ["OR", "RO", "OY", "YO"]:
				assert wrapped.count(s) == 0, wrapped
			for s in ["VR", "RV", "VB", "BV"]:
				assert wrapped.count(s) == 0, wrapped
	print "Case #%s: %s"%(test_case+1, answer)
