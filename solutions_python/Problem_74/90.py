input = open("BotTrust.in")
output = open("BotTrust.out", "w")
T = int(input.readline())
def other(o):
	return "B" if o == "O" else "O"

for t in range(T):
	sequence = input.readline()
	sequence = sequence.split(" ")[1:]
	sequence = [{"color": sequence[i], "position": int(sequence[i + 1])} for i in range(0, len(sequence), 2)]
	next = {"O": None, "B": None}
	for move in reversed(sequence):
		move["next"] = next[other(move["color"])]
		next[move["color"]] = move
	pos = {"O": 1, "B": 1}
#	print(sequence)
	moves = 0
	for move in sequence:#, sequence[1:] + [None]:
		m = abs(pos[move["color"]] - move["position"]) + 1
		if move["next"] is not None:
			next = move["next"]
			o = other(move["color"])
			delta = min(abs(pos[o] - next["position"]), m)
			direction = -1 if pos[o] > next["position"] else 1
			pos[o] += delta * direction
		pos[move["color"]] = move["position"]
		moves += m
#		print(pos["O"], pos["B"], moves)
	print("Case #{case}: {moves}".format(case = t + 1, moves = moves), file = output)
output.close()