#Problem A

def solved(pancakes):
	return pancakes.count('+') == len(pancakes)

#def parity(pancakes, k):
#	if (pancakes.count('+') % k != 0):
#		return True
#	return False

def opposite(c):
	if c == '+':
		return '-'
	return '+'
	
def solve(pancakes, k):
	pancakes = list(pancakes)
	if solved(pancakes):
		return 0
	#if parity(pancakes, k):
	#	return "IMPOSSIBLE"
	numFlips = 0
	while not(solved(pancakes)):
		firstIndex = pancakes.index('-')
		for i in range(k):
			if(i+firstIndex >= len(pancakes)):
				return "IMPOSSIBLE"
			pancakes[i+firstIndex] = opposite(pancakes[i+firstIndex])
		numFlips += 1
	return numFlips

	
	
def main():
	f = open("A-large.IN", "r")

	numCases = int(f.readline())

	for i in range(numCases):
		#parse line
		line = f.readline().split(' ')
		pancakes = line[0]
		k = int(line[1])
		
		#solve
		#print result
		print("Case #", i+1, ": ", solve(pancakes, k), sep='')
	

main()