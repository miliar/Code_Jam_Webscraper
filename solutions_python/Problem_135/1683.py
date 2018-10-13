def get_row():
	guess = input()
	cards = [map(int, raw_input().split()) for _ in range(4)]
	return cards[guess - 1]

def find_card(r1, r2):
	intersection = [i for i in r1 if i in r2]
	if len(intersection) > 1:
		return "Bad magician!"
	if len(intersection) == 0:
		return "Volunteer cheated!"
	return intersection[0]

cases = input()

for i in range(1, cases + 1):
	row1 = get_row()
	row2 = get_row()
	result = find_card(row1, row2)
	print "Case #{0}: {1}".format(i, result)
