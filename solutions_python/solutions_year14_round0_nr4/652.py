#
# Google Code Jam 2014
# Problem D: Deceitful War
# 
# Solved by Michael Oliver (a.k.a. The Code Boss)
# April 11, 2014
#

# Helpers
def FirstGreaterThan(lis, n):
	for index, element in enumerate(lis):
		if element > n:
			return index
	return -1
	
def PlayNormalWar(Naomi, Ken):
	N_Score = 0
	K_Score = 0
	while len(Naomi) > 0:
		KenLowest = Ken[0]
		KenHighest = Ken[len(Ken)-1]
		NaomiLowest = Naomi[0]
		NaomiHighest = Naomi[len(Naomi)-1]
		if NaomiLowest > KenHighest:
			# She just wins the rest
			N_Score += len(Naomi)
			break
		if NaomiHighest > KenHighest:
			# Play it and get it over with
			Ken = Ken[1:]
			Naomi = Naomi[:-1]
			N_Score += 1
		elif NaomiLowest > KenLowest:
			# Then play it, and Ken will play something higher if
			# he has it
			Naomi = Naomi[1:]
			kindex = FirstGreaterThan(Ken, NaomiLowest)
			if kindex == 0:
				Ken = Ken[1:]
			elif kindex > 0 and kindex < len(Ken)-1:
				Ken = Ken[0:kindex] + Ken[kindex+1:]
			elif kindex == len(Ken)-1:
				Ken = Ken[:-1]
			else:
				Ken = Ken[1:]
				N_Score += 1
		elif NaomiLowest < KenLowest:
			# No choice, there's no way she can win that one
			# Wait for Ken to use up all his low ones before playing
			# this so that he is forced to use high ones?
			Ken = Ken[1:]
			Naomi = Naomi[1:]
	return N_Score
	
def PlayDeceitfulWar(Naomi, Ken):
	N_Score = 0
	while len(Naomi) > 0:
		KenLowest = Ken[0]
		KenHighest = Ken[len(Ken)-1]
		NaomiLowest = Naomi[0]
		if NaomiLowest < KenLowest:
			# Lie and get him to get rid of his highest
			Ken = Ken[:-1]
			Naomi = Naomi[1:]
			continue
		elif NaomiLowest > KenHighest:
			# Naomi auto-wins the rest of the games
			N_Score += len(Naomi)
			break
		else:
			# Naomi plays her smallest, but says its very high
			# so that Ken gets rid of his lowest
			Naomi = Naomi[1:]
			Ken = Ken[1:]
			N_Score += 1
	return N_Score

# Main program
NumTests = int(input())

for TestNumber in range(1,NumTests+1):

	N = int(input())
	Naomi = sorted(map(lambda x: float(x), input().split()))
	Ken = sorted(map(lambda x: float(x), input().split()))
	
	a = PlayNormalWar(Naomi, Ken)
	b = PlayDeceitfulWar(Naomi, Ken)
	print('Case #%d: %d %d' % (TestNumber, b, a))