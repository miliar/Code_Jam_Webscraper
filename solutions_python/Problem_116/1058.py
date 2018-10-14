n=""
def f(a): 
	if a==".":return 0
	if a=="T":return 10
	if a=="O":return 1
	if a=="X":return -1
def g(a): return sum(map(lambda x:f(x),list(a))) 
def h(tablero):
	lineas=[]
	lineas.append(tablero[0])
	lineas.append(tablero[1])
	lineas.append(tablero[2])
	lineas.append(tablero[3])
	for i in range(0,4):
		lineas.append(tablero[0][i]+tablero[1][i]+tablero[2][i]+tablero[3][i])
	lineas.append(tablero[0][0]+tablero[1][1]+tablero[2][2]+tablero[3][3])
	lineas.append(tablero[0][3]+tablero[1][2]+tablero[2][1]+tablero[3][0])
	return lineas
				
def k(tablero,case):
	incomplete=0
	lineas=h(tablero)
	global n
	for a in lineas:
		A=g(a)
		if A==7 or A==-4:
			n=n+"Case #"+str(case)+": X won"+"\n"
			return 0
		if A==13 or A==4:
			n+="Case #"+str(case)+": O won"+"\n"
			return 0
		if "." in a:incomplete=1
	if incomplete==1:
		n+="Case #"+str(case)+": Game has not completed"+"\n"
		return 0
	n+="Case #"+str(case)+": Draw"+"\n"
	return 0
T=int(raw_input())
for j in xrange(1,T+1):
	a_1=raw_input()
	a_2=raw_input()
	a_3=raw_input()
	a_4=raw_input()
	a_5=raw_input()
	tablero=[a_1,a_2,a_3,a_4]
	k(tablero,j)
print n
