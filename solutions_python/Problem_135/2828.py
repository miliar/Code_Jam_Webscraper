import sys

ATTEMPT_NO = 1

def solve(configs):
	row_choices = [set(c[k - 1]) for (k,c) in configs]
	soln = row_choices[0].intersection(row_choices[1])

	if len(soln) == 0:
		result = "Volunteer cheated!"
	elif len(soln) != 1:
		result = "Bad magician!"
	else:
		result = str(list(soln)[0])
	return result

def get_cards(f):
	cards = []
	for _ in range(0,4):
		temp = f.readline().split()
		cards.append([int(x) for x in temp])
	return cards

def get_config(f):
	choice = int(f.readline())
	cards = get_cards(f)
	return (choice, cards)

if __name__ == '__main__':
	sys.stdout = open("A-small-attempt%d.out" % ATTEMPT_NO, "w+")
	f = open("A-small-attempt%d.in" % ATTEMPT_NO)
	T = int(f.readline())

	for c in range(1, T + 1):
		configs = [get_config(f), get_config(f)]
		result = solve(configs)
		print("Case #%d: %s" %(c, result))




