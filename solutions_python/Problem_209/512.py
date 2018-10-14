PIE = 3.1415926535897932384626433832795028841971

def calc_up(rad):
	global PIE
	return (rad ** 2) * PIE
def calc_side(rad, height):
	global PIE
	return 2*rad*PIE*height

def calc(stack):
	sumv = 0
	for rad, height in stack:
		sumv += calc_side(rad, height)
	sumv += calc_up(stack[0][0])
	return sumv

def judge_stack(pancakes, count):
	sorted_pancakes = [(pancake[1], pancake[2]) for pancake in sorted([(calc_side(*pancake), pancake[0], pancake[1]) for pancake in pancakes])[::-1]]
	stack = sorted_pancakes[:count-1]
	return stack

def solve(pancakes, count):
	pancakes = sorted(pancakes)[::-1]
	# max_height_index = -1
	# max_height = -1
	# for i in range(len(pancakes)):
	# 	if max_height < pancakes[i][1]:
	# 		max_height = pancakes[i][1]
	# 		max_height_index = i
	max_res = -1
	# # print(pancakes)
	for top in range(len(pancakes)):
		# print("top = {0}, len(pancakes) = {1}".format(top, len(pancakes)))
		stack = [pancakes[top],]
		copycakes = pancakes[:]
		del copycakes[top]
		copycakes = [pancake for pancake in copycakes if pancake[0] <= pancakes[top][0]]
		if len(copycakes) < count-1:
			break
		stack += judge_stack(copycakes, count)
		res = calc(stack)
		if res > max_res:
			max_res = res
	return max_res
	
if __name__ == '__main__':
	tc = int(input())
	for tci in range(1, tc+1):
		N, K = map(int, input().strip().split())
		pancakes = []
		for pancake in range(N):
			rad, height = map(int, input().strip().split())
			pancakes.append((rad, height))
		res = solve(pancakes, K)
		print("Case #{0}: {1}".format(tci, res))

"""
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
"""