history = []
def flip(lineup, mask):
	ret = lineup ^ mask
	return ret

def result(lineup, mask, goal):
	if lineup in history:
		return 'IMPOSSIBLE'
	if lineup == goal:
		return 0
	history.append(lineup)
	while mask <= goal:
		lineup2 = flip(lineup, mask)
		res = result(lineup2, mask, goal)
		if res != 'IMPOSSIBLE':
			return res + 1 
		mask <<= 1

	return 'IMPOSSIBLE'


a = int(input())
for i in range(a):
	lineup, num = input().split()
	goal = eval('0b' + '1' * len(lineup))
	lineup = eval('0b' + lineup.replace('-', '0').replace('+', '1'))
	mask = eval('0b' + '1' * int(num))
	print("Case #%d: %s" % (i+1, result(lineup, mask, goal)))
	history = []