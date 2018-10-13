for case in range(int(input())):
	num_row = int(input())
	rows = []
	for row in range(4):
		rows.append(input().split())
	cards = rows[num_row - 1]
	num_row = int(input())
	rows = []
	for row in range(4):
		rows.append(input().split())
	cards = list(filter(lambda card: card in rows[num_row - 1], cards))
	if len(cards) == 0:
		answer = "Volunteer cheated!"
	elif len(cards) == 1:
		answer = cards[0]
	else:
		answer = "Bad magician!"
	print("Case #%d: %s" % (case + 1, answer))