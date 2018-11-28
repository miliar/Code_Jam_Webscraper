import string 

def solve(senators):
	evacuation = []
	senators = map(int, senators.split())
	sen_len = sum(senators)
	while sum(senators) > 0:
		indexes = list(reversed(sorted(range(len(senators)), key=lambda k: senators[k])))
		if senators[indexes[0]] == senators[indexes[1]]:
			evacuation = evacuation + [indexes[0], indexes[1]]
			senators[indexes[0]] -= 1
			senators[indexes[1]] -= 1
		else:
			evacuation = evacuation + [indexes[0], indexes[0]]
			senators[indexes[0]] -= 2

	letters = map(lambda x: string.ascii_uppercase[x], evacuation[:sen_len])
	if len(letters) % 2 == 0:
		return ' '.join([''.join(letters[i:i+2]) for i in range(0, len(letters), 2)])
	else:
		letters_from_second = letters[1:]
		return letters[0] + ' ' + ' '.join([''.join(letters_from_second[i:i+2]) for i in range(0, len(letters_from_second), 2)])




if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		number_of_senate = input()
		senators = raw_input()
		print("Case #%i: %s" % (caseNr, solve(senators)))
		