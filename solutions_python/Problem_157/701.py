#MAM, Google Code Jam - Qualification Round, Problem 3

def quatern(a, signa, b, signb = 1):
	if a == "1":
		if b == "1":
			return "1", signa * signb
		if b == "i":
			return "i", signa * signb
		if b == "j":
			return "j", signa * signb
		if b == "k":
			return "k", signa * signb

	if a == "i":
		if b == "1":
			return "i", signa * signb
		if b == "i":
			return "1", signa * signb * -1
		if b == "j":
			return "k", signa * signb
		if b == "k":
			return "j", signa * signb * -1

	if a == "j":
		if b == "1":
			return "j", signa * signb
		if b == "i":
			return "k", signa * signb * -1
		if b == "j":
			return "1", signa * signb * -1
		if b == "k":
			return "i", signa * signb

	if a == "k":
		if b == "1":
			return "k", signa * signb
		if b == "i":
			return "j", signa * signb
		if b == "j":
			return "i", signa * signb * -1
		if b == "k":
			return "1", signa * signb * -1

def solve(L, X, text):
	text = text * X

	GOAL1 = "i"
	GOAL2 = "j"
	GOAL3 = "k"

	step1 = False
	step2 = False
	step3 = False

	position = 0
	curr = text[position]
	currsign = 1
	position += 1

	for eachc in text[position:]:
		if curr == GOAL1 and currsign == 1:
			step1 = True
			break
		else:
			curr, currsign = quatern(curr, currsign, eachc)
			position += 1

	if step1 == False:
		return "NO"


	curr = text[position]
	currsign = 1
	position += 1

	for eachc in text[position:]:
		if curr == GOAL2 and currsign == 1:
			step2 = True
			break
		else:
			curr, currsign = quatern(curr, currsign, eachc)
			position += 1

	if step2 == False:
		return "NO"

	curr = text[position]
	currsign = 1
	position += 1

	for eachc in text[position:]:
		curr, currsign = quatern(curr, currsign, eachc)

	if curr == GOAL3 and currsign == 1:
		step3 = True

	if step3:
		return "YES"

	return "NO"

def main():
	with open('C-small-attempt0.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			L, X = [int(i) for i in infile.readline().rstrip().split(" ")]
			text = infile.readline().rstrip()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(L, X, text)) + "\n")

if __name__ == "__main__":
	main()