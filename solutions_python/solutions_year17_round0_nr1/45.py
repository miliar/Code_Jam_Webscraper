import sys
import itertools

#filename = "test.in"
filename = None

def is_happy(S):
	return all(pancake == "+" for pancake in S)


def flipped(sequence):
	opposite = {
		"+" : "-",
		"-" : "+"
	}
	return map(lambda x: opposite[x], sequence)

def simplify(S,k):
	while(True):
		print S[0:k]
		if S[0:k] == "+"*k:
			S=S[k:]
			continue
		return S

def flip(S, k, i):
	if i+k > len(S):
		raise Exception("Cannot flip beyond the edge")
	tmp = list(S)
	tmp[i:i+k] = flipped(tmp[i:i+k])
	return tmp

def solve(i, S, k):
	l = len(S)
	nb_flip = 0
	for i in range(l-k+1):
		if(S[i] == "-"):
			S = flip(S,k,i)
			nb_flip +=1

	if is_happy(S):
		return nb_flip
	else:
		return "IMPOSSIBLE"


def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for i in range(T):	
		S, k = file.readline().strip().split()
		k = int(k)
		answer = solve(i, S, k)
		print "Case #%d: %s" % (i+1, answer)
		#print_case(i, N, M, customers)
		

	if file is not sys.stdin:
	    file.close()

def main2():
	assert solve(1,"-+-+-",4) == "IMPOSSIBLE"
	assert solve(2,"---+-++-", 3) == 3
	

if __name__ == '__main__':
	main()
	#main2()
