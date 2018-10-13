import bisect

def war(b1, n1, k1):
	score = 0
	for i in range(0, b1):
		index = bisect.bisect_left(k1, n1[i])
		if index == len(k1):
			score = score+1
			k1.remove(k1[index-1])
		else:
			k1.remove(k1[index])
	return score

def deceitful(b2, n2, k2):
	score = 0
	for i in range(0, b2):
		if (bisect.bisect_left(k2, n2[i]) == 0):
			k2.remove(k2[len(k2)-1])
		else:
			score = score+1
			k2.remove(k2[0])
	return score

text = open("D-large.in.txt", "r")
k = int(text.readline())
for l in range(1,k+1):
	blocks = int(text.readline())
	naomi = sorted(map(float, text.readline().split(' ')))
	ken = sorted(map(float, text.readline().split(' ')))
	n1 = naomi[:]
	n2 = naomi[:]
	k1 = ken[:]
	k2 = ken[:]
	print('Case #'+str(l)+': '+str(deceitful(blocks, n1, k1))+' '+str(war(blocks, n2, k2)))