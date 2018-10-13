def flip(S, K, i):

	for j in range(K):
		if S[i] == "+":
			S[i] = "-"
		else:
			S[i] = "+"
		i += 1
	return S


def solve(S, K):
	r = 0
	for i in range(len(S)-K+1):
		if S[i] == '-':
			S = flip(S, K, i)
			r += 1
		

	if S.count("+") == len(S):
		return str(r)
	else:
		return "IMPOSSIBLE"



def main():

	T = int(raw_input())
	responses = list()
	for t in xrange(T):

		raw = raw_input().split(" ")

		S = list(raw[0])
		K = int(raw[1])

		responses.append(solve(S, K))

	i = 0
	for r in responses:
		i+=1
		print "Case #"+str(i)+": "+str(r)

if __name__ == "__main__":
	main()