from sys import stdin

def check_winning(naomi,ken):
	result = 0
	for x,y in zip(naomi, ken):
		if x > y:
			result += 1
	return result

def check_normal_wins(naomi, ken):
	ken = sorted(ken)
	for n in sorted(naomi):
		next_largest = 0
		for k in ken:
			if k > n:
				next_largest=k
				break
		if next_largest == 0:
			return len(ken)
		else:
			ken.remove(k)
	return 0


def main():
	T = int(stdin.readline())
	for t in xrange(1,T+1):
		N = int(stdin.readline())
		naomi = sorted([float(x) for x in stdin.readline().strip().split(" ")], reverse=True)
		ken = sorted([float(x) for x in stdin.readline().strip().split(" ")], reverse=True)
		normal_wins = check_normal_wins(naomi, ken)
		while check_winning(naomi,ken) != N:
			# print "not winning"
			# print naomi
			# print ken
			naomi = naomi[:-1]
			ken = ken[1:]
			N-=1
		# print "winning - %d"%N
		# print naomi
		# print ken
		print "Case #%d:"%t, N, normal_wins


if __name__ == '__main__':
	main()