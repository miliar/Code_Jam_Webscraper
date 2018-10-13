# get surprise on minimum
# mod 0 -> d/3-1 + d/3+1 + d/3, min d/3-1
# mod 1 -> doesn't exist
# mod 2 -> d/3 + d/3 + d/3+2, min d/3

# non-surprising
# mod 0 -> d/3, min d/3
# mod 1 -> d/3 + d/3 + d/3+1, min d/3, max d/3+1
# mod 2 -> d/3+1 + d/3+1 + d/3, min d/3 max d/3+1

# set surprising on lowest not mod 1
def s_max_possible(n):
	if n == 2:
		return 2
	elif n%3 == 0:
		return n/3+1
	else:
		return n/3+2

def max_possible(n):
	if n < 2:
		return n
	elif n == 2:
		return 1
	elif n%3 == 0:
		return n/3
	else:
		return n/3+1

def main():
	input = open("B-large.in", "r").readlines()
	T = int(input[0])
	for t in range(1, T + 1):
		l = input[t].split()
		N, S, p, l = int(l[0]), int(l[1]), int(l[2]), [int(x) for x in l[3:]]
		l.sort()
		for i in range(0, N):
			if S > 0:
				if l[i] > 1 and l[i] < 29 and l[i]%3 != 1:
					if s_max_possible(l[i]) >= p:
						l[i] = s_max_possible(l[i])
						S -= 1
						continue
			l[i] = max_possible(l[i])
		print "Case #%d: %s" % (t, sum([x >= p for x in l])) 

if __name__ == "__main__":
	main()
