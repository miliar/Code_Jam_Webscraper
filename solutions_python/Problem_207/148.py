import fileinput
import sys

def debug(s):
	#print >> sys.stderr, s
	#sys.stderr.flush()
	pass

YELLOW = "Y"
RED = "R"
BLUE = "B"
ORANGE = "O"
GREEN = "G"
VIOLET = "V"

count = int(raw_input())
case = 0

while True:
	case += 1
	if count < case:
		break

	N, R, O, Y, G, B, V = map(int, raw_input().split())
	debug([N, R, O, Y, G, B, V])

	if 0 < B and 0 < O and B == O:
		if 0 < R or 0 < Y or 0 < G or 0 < V:
			debug("B == O with other stuff")
			print "Case #%s: IMPOSSIBLE" % case
		else:
			solution = [BLUE, ORANGE] * B
			print "Case #%s: %s" % (case, "".join(solution))
		continue

	if 0 < R and 0 < G and R == G:
		if 0 < B or 0 < Y or 0 < O or 0 < V:
			debug("R == G with other stuff")
			print "Case #%s: IMPOSSIBLE" % case
		else:
			solution = [RED, GREEN] * R
			print "Case #%s: %s" % (case, "".join(solution))
		continue

	if 0 < Y and 0 < V and Y == V:
		if 0 < R or 0 < B or 0 < G or 0 < O:
			debug("Y == V with other stuff")
			print "Case #%s: IMPOSSIBLE" % case
		else:
			solution = [YELLOW, VIOLET] * Y
			print "Case #%s: %s" % (case, "".join(solution))
		continue

	if 0 < O and B <= O:
		debug("not enough B to surround the O")
		print "Case #%s: IMPOSSIBLE" % case
		continue
	if O != 0:
		B -= (O + 1) # reserve enough to surround

	if 0 < G and R <= G:
		debug("not enough R to surround the G")
		print "Case #%s: IMPOSSIBLE" % case
		continue
	if G != 0:
		R -= (G + 1) # reserve enough to surround

	if 0 < V and Y <= V:
		debug("not enough Y to surround the V")
		print "Case #%s: IMPOSSIBLE" % case
		continue
	if V != 0:
		Y -= (V + 1) # reserve enough to surround

	numberOfBlueBlocks = B + (0 if O == 0 else 1)
	numberOfRedBlocks = R + (0 if G == 0 else 1)
	numberOfYellowBlocks = Y + (0 if V == 0 else 1)

	solution = []
	lastColor = YELLOW # just something to start with
	firstColor = None # TODO first and last color must be different
	while 0 < numberOfBlueBlocks or 0 < numberOfRedBlocks or 0 < numberOfYellowBlocks:
		debug("Blocks: B %s, R %s, Y %s" % (numberOfBlueBlocks, numberOfRedBlocks, numberOfYellowBlocks))
		if lastColor == YELLOW:
			if numberOfBlueBlocks < numberOfRedBlocks or (numberOfBlueBlocks == numberOfRedBlocks and firstColor == RED):
				# gotta put red
				if G != 0:
					solution += [RED, GREEN] * G + [RED]
					G = 0
				else:
					solution += [RED]
					R -= 1
				numberOfRedBlocks -= 1
				lastColor = RED
				if firstColor is None:
					firstColor = RED
			else:
				# gotta put blue
				if O != 0:
					solution += [BLUE, ORANGE] * O + [BLUE]
					O = 0
				else:
					solution += [BLUE]
					B -= 1
				numberOfBlueBlocks -= 1
				lastColor = BLUE
				if firstColor is None:
					firstColor = BLUE
		elif lastColor == RED:
			if numberOfBlueBlocks < numberOfYellowBlocks or (numberOfBlueBlocks == numberOfYellowBlocks and firstColor == YELLOW):
				# gotta put yellow
				if V != 0:
					solution += [YELLOW, VIOLET] * V + [YELLOW]
					V = 0
				else:
					solution += [YELLOW]
					Y -= 1
				numberOfYellowBlocks -= 1
				lastColor = YELLOW
				if firstColor is None:
					firstColor = YELLOW
			else:
				# gotta put blue
				if O != 0:
					solution += [BLUE, ORANGE] * O + [BLUE]
					O = 0
				else:
					solution += [BLUE]
					B -= 1
				numberOfBlueBlocks -= 1
				lastColor = BLUE
				if firstColor is None:
					firstColor = BLUE
		elif lastColor == BLUE:
			if numberOfRedBlocks < numberOfYellowBlocks or (numberOfRedBlocks == numberOfYellowBlocks and firstColor == YELLOW):
				# gotta put yellow
				if V != 0:
					solution += [YELLOW, VIOLET] * V + [YELLOW]
					V = 0
				else:
					solution += [YELLOW]
					Y -= 1
				numberOfYellowBlocks -= 1
				lastColor = YELLOW
				if firstColor is None:
					firstColor = YELLOW
			else:
				# gotta put red
				if G != 0:
					solution += [RED, GREEN] * G + [RED]
					G = 0
				else:
					solution += [RED]
					R -= 1
				numberOfRedBlocks -= 1
				lastColor = RED
				if firstColor is None:
					firstColor = RED

	if len(solution) == 0 or solution[0] == solution[-1] or numberOfBlueBlocks < 0 or numberOfRedBlocks < 0 or numberOfYellowBlocks < 0:
		print "Case #%s: IMPOSSIBLE" % case
		continue

	print "Case #%s: %s" % (case, "".join(solution))
