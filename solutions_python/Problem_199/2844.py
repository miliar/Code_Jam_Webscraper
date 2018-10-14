def areAllHappy(S):
	for i in range(0, len(S)):
		if S[i] == '-':
			return False;
	return True;

def flip(S, K, i):
	for pos in range(i, i+K):
		if S[pos] == '+':
			S[pos] = '-'
		elif S[pos] == '-':
			S[pos] = '+'
	return S

def solve(S, K):
	flips = 0;
	for i in range(0, len(S) - K+1):
		if S[i] == '-':
			S = flip(S, K, i);
			flips = flips +1;
	if areAllHappy(S):
		return str(flips);
	else:
		return "IMPOSSIBLE"


T = input();

for t in range(1, T+1):
    SK = raw_input();
    SK = SK.split(" ");
    S = list(SK[0]);
    K = int(SK[1]);

    res = solve(S, K);
    print "Case #"+str(t)+": "+str(res);

