def flip(x):
	a = ''
	for y in x:
		if y == "+":
			a = a + '-'
		if y == "-":
			a = a + '+'
	return str(a)

def solveproblem(P,F):

	N = len(P)
	ans = 0

	for j in range(N-F+1):
		if P[j] == '-':
			
			# print "***"
			# print flip(P[j+1:j+F])
			# print N, P, j, F, P[j+1:j+F], flip(P[j+1:j+F]), P[j+F:], P[:j]
			# print P[:j] + '+' + flip(P[j+1:j+F]) + P[j+F:]
			# print "***"

			if F == 1:
				P = str(P[:j]) + '+' + str(P[j+F:])
			else:
				P = str(P[:j]) + '+' + flip(P[j+1:j+F]) + str(P[j+F:])
			ans += 1
			# print P
	

	if "-" in P:
		return "impossible"
	else:
		return str(ans)




def solvecases():
	n = int(raw_input())
	for j in range(n):
		pancakes, flipper = raw_input().strip().split(" ")

		print "Case #" + str(j+1) + ": " + solveproblem(pancakes,int(flipper))
		
solvecases()