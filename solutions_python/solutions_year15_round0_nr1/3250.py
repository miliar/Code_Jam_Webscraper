import sys

def invite_friends(s_max, audience):
	audiences = [int(ch) for ch in audience]

	friends = 0

	for i in range(1, s_max + 1):
		diff = i - (sum(audiences[0:i]) + friends)

		if diff > 0:
			friends = friends + diff

	return friends

def main():
	filename = sys.argv[1:]
	f = open(filename[0])

	test_case = int(f.readline())

	for case in range(test_case):
		line = f.readline()
		parts = line.split()

		s_max = parts[0]
		audience = parts[1]

		friends = invite_friends(int(s_max), audience)

		print 'Case #{0}: {1}'.format(int(case) + 1, friends)

if __name__ == '__main__':
	main()