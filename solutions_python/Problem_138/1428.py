
input = open('./D-large.in', 'r')
output = open('./out', 'w')

def optimalWarScore(naomi, ken):
	N = len(ken)
	naomi_sorted = sorted(naomi)
	ken_sorted = sorted(ken)
	score = 0
	for i in range(N):
		naomi_block = naomi_sorted[i]
		ken_block = -1.0
		for j in range(len(ken_sorted)):
			if ken_sorted[j] > naomi_block:
				ken_block = ken_sorted.pop(j)
				break
		if ken_block < 0:
			score += 1
	return score

def deceitfulWarScore(naomi, ken):
	N = len(ken)
	naomi_sorted = sorted(naomi)
	ken_sorted = sorted(ken)
	score = 0
	while len(naomi_sorted)>0:
		naomi_block = naomi_sorted.pop(0)
		if naomi_block > ken_sorted[0]:
			ken_sorted.pop(0)
			score += 1 
	return score

num_cases = int(input.readline())
for case in range(num_cases):
	output.write("Case #"+str(case+1)+": ")
	N = int(input.readline())
	naomi = input.readline().split()
	ken = input.readline().split()
	for i in range(N):
		naomi[i] = float(naomi[i])
		ken[i] = float(ken[i])

	output.write(str(deceitfulWarScore(naomi, ken)) + " "+ str(optimalWarScore(naomi, ken)))
	output.write("\n")

input.close()
output.close()

