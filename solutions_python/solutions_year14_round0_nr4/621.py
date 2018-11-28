from bisect import bisect

def war(p1, p2):
	score = 0
	while p1:
		block = p1.pop()
		pos = bisect(p2, block)
		if pos == len(p2):
			del p2[0]
			score += 1
		else:
			del p2[pos]
	return score

def deceitfulWar(p1, p2):
	score = 0
	while p1:
		if p1[0] > p2[0]:
			del p1[0]
			del p2[0]
			score += 1
		else:
			del p1[0]
			del p2[-1]
	return score
	
def solver():
	input()
	p1 = sorted([float(i) for i in input().split()])
	p2 = sorted([float(i) for i in input().split()])
	return deceitfulWar(p1.copy(), p2.copy()), war(p1.copy(), p2.copy())

def main():
	t = int(input())
	for i in range(1, t + 1):
		solution = solver()
		print("Case #{:d}: {:d} {:d}".format(i, *solution))

if __name__ == "__main__":
	main()	
		