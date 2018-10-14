import sys
import itertools

#filename = "test.in"
filename = None
#filename = "B-small-attempt2.in"


def solve(casenum, N, R, O, Y, G, B, V):
	cols = {
		"R": R,
		"Y": Y,
		"B": B,
	}

	l = cols.items()
	l.sort(key=lambda x: x[1])
	A = l[0]
	B = l[1]
	C = l[2]

	if C[1] <= (2*A[1] + B[1] - A[1]):
		c_moins_b_moins_a = C[1]-(B[1]-A[1])
		coef1 = B[1]-A[1]
		coef2 = (c_moins_b_moins_a)/2
		coef3 = A[1]-(c_moins_b_moins_a/2)

		cb = C[0]+B[0]
		cacb = C[0]+A[0]+C[0]+B[0]
		ab = A[0]+B[0]
		c = C[0]
		
		if c_moins_b_moins_a % 2 == 1:
			if  coef3 != 0 :
				answer= coef1*cb + coef2*cacb + c + coef3*ab
			else:
				answer = "IMPOSSIBLE"
			
		else:
			answer= coef1*cb + coef2*cacb + coef3*ab

		#CHECK ANSWER 
		# if (answer != "IMPOSSIBLE"):
		# 	if len([x for x in answer if x==A[0]]) != A[1]:
		# 		print answer
		# 		print coef1, coef2, coef3, c_moins_b_moins_a
		# 		print A, B, C
		# 	assert(len([x for x in answer if x==A[0]]) == A[1])
		# 	assert(len([x for x in answer if x==B[0]]) == B[1])
		# 	assert(len([x for x in answer if x==C[0]]) == C[1])

		# 	for x in range(len(answer)):
		# 		if answer[x] == answer[x-1]:
		# 			print answer, x
		# 			print A, B, C
		# 			raise Exception("found")



	else:
		answer= "IMPOSSIBLE"

	print "Case #%d: %s" % (casenum, answer)
		


def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for casenum in range(1, T+1):	
		N, R, O, Y, G, B, V = map(int, file.readline().strip().split())
		solve(casenum, N, R, O, Y, G, B, V)
		

	if file is not sys.stdin:
	    file.close()



if __name__ == '__main__':
	main()
