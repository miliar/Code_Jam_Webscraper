def naomi_wins_tricky(Naomi, Ken, t):
	score = 0
	while (t > 0):
		if Naomi[0] < Ken[0]:
			Naomi = Naomi[1:]
			Ken = Ken[:-1]
		else:
			Naomi = Naomi[1:]
			Ken = Ken[1:]
			score += 1
		t-=1

	return score

def naomi_wins_usual(Naomi, Ken, t):
	score = 0
	while (t > 0):
		NaomiX = Naomi[-1]
		Naomi = Naomi[:-1]
		if (NaomiX > Ken[-1]):
			score += 1
			Ken = Ken[1:]
		else:
			for i in xrange(t-1, -1, -1):
				if (Ken[i] > NaomiX):
					Ken = Ken[:i] + Ken[i+1:]
					break;

		t-=1

	return score

def process_case(case_number):
	T = int(raw_input())
	Naomi = []
	Ken = []

	NaomiString = raw_input()
	NaomiListS = NaomiString.split(' ')
	Naomi = map(float, NaomiListS)

	KenString = raw_input()
	KenListS = KenString.split(' ')
	Ken = map(float, KenListS)

	Naomi.sort()
	Ken.sort()

	print "Case #{0}:".format(case_number), naomi_wins_tricky(Naomi, Ken, T), naomi_wins_usual(Naomi, Ken, T)

N = int(raw_input())

for i in xrange(0, N):
	process_case(i + 1)

#print N