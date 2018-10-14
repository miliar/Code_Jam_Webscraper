import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		sys.stderr.write('processing case %d\n' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	n = int(sys.stdin.readline().strip())
	naomi = map(float, sys.stdin.readline().split())
	naomi.sort()
	naomi.reverse()
	ken = map(float, sys.stdin.readline().split())
	ken.sort()
	ken.reverse()
	d_score = get_deceitful_score(naomi[:], ken[:])
	n_score = get_normal_score(naomi[:], ken[:])
	sys.stdout.write('Case #%d: %s %s\n' % (case, str(d_score), str(n_score)))

def get_deceitful_score(naomi, ken):
	score = 0
	while len(naomi) > 0 or len(ken) > 0:
		if ken[0] > naomi[0]:
			naomi.pop()
			ken.pop(0)
		else:
			naomi.pop(0)
			ken.pop(0)
			score = score + 1
	return score

def get_normal_score(naomi, ken):
	score = 0
	while len(naomi) > 0 or len(ken) > 0:
		n = naomi.pop(0)
		ken_won = False
		for i in range(len(ken) - 1, -1, -1):
			if ken[i] > n:
				ken.pop(i)
				ken_won = True
				break
		if not ken_won:
			ken.pop()
			score = score + 1
	return score

if __name__ == '__main__':
	main()
