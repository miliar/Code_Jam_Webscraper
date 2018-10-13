#flips a pancake
def flip_one(pancakes, pos) : 
	if pancakes[pos] == '+':
		pancakes[pos] = '-'
	else :
		pancakes[pos] = '+'

#flips the K pancakes at position pos 
def flip(pancakes,K,pos) :
	for i in range(K) : 
		flip_one(pancakes, pos + i)

#solves the problem for one entry
def solve(pancakes,K) : 
	sol = 0
	index = 0
	for index in range(len(pancakes) - (K - 1)) :
		char = pancakes[index]
		if char == '-':
			flip(pancakes,K,index)
			sol += 1
		index += 1
	
	for i in range((len(pancakes)- 1 ) - (K - 1), len(pancakes)) :
		if pancakes[i] == '-' :
			return 'IMPOSSIBLE'
	return str(sol)


f = open('test2.in', 'r')
l = f.readlines()
size = l[0]
for i in range(1,int(size) + 1):
	splitted = str.split(l[i])
	res = solve(list(splitted[0]),K = int(splitted[1]))
	print ('Case #' + str(i) + ': ' + res)
