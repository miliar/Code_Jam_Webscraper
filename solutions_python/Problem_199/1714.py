
def isGood(cake):
	if cake.count("-") == 0:
		return True
	else:
		return False

def flip(side):
	if side == "+": return "-"
	if side == "-": return "+"

def flip_cake(cake, start, pan):
	if start+pan > len(cake):
		return ""
	
	new_cake = ""
	for i in range(0, len(cake)):
		if i >= start and i < start+pan:
			new_cake += flip(cake[i])
		else:
			new_cake += cake[i]
	return new_cake

best_depth = 100000000
found = False
searched = dict() 

def DFS(pair, pan): # pair[0] = cake, pair[1] = depth
	global best_depth
	global searched
	global found
	
#	print("Searching {} in depth {}".format(pair[0], pair[1])) # debug
	if pair[0] in searched and pair[1] >= searched[pair[0]]:
		return
	if pair[1] >= best_depth:
		return
	if isGood(pair[0]):
		if best_depth > pair[1]:
			best_depth = pair[1]
		found = True
		return

	lst = []
	size = len(pair[0])

	searched[pair[0]] = pair[1]
	for i in range(0, size):
		new_cake = flip_cake(pair[0], i, pan)
		if new_cake != "":
			DFS((new_cake, pair[1]+1), pan)


def work(cake, pan):
	global best_depth
	global searched
	global found
	
	searched = dict()
	best_depth = 100000000
	found = False

	# use a breadth-first search
	# use a depth-first search insead
	DFS((cake, 0), pan)


	return (best_depth, found) 

# Main section
t = int(input())

for i in range(1, t+1):
	cake, pan = input().split(" ")
	size = int(pan)
#	print("{} size={}".format(cake, size)) # debug
	answer = work(cake, size)
	if answer[1] == False:
		print("Case #{}: IMPOSSIBLE".format(i))
	else:
		print("Case #{}: {}".format(i, answer[0]))
	
