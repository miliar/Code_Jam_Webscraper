T = int(raw_input())

#reverse list mark looser/winner
#if winner, metra posous loosers exei mprosta tou: tosa swaps thelei aytos o winner
#sort winners by swaps (increasing)
#an winners < K impossible
#swaps = sum ta swaps twn K prwtwn winners

for cases in range(1,T+1):
	res = ''
	N, K, B, T = map(int, raw_input().split())
	Xi = map(int, raw_input().split())
	Vi = map(int, raw_input().split())

	winners = [] # posous loosers mprosta tou
	loosers = [] # Xi of looser
	for chicken in range(N-1,-1,-1):
		if (0.0+B-Xi[chicken])/(0.0+Vi[chicken]) <= T:
			winners.append(len(loosers))
		else:
			loosers.append(Xi[chicken])

	winners.sort()
	if len(winners) < K:
		res = "IMPOSSIBLE"
	else:
		res = str(sum(winners[0:K]))

	print "Case #%d: %s" %(cases, res)
