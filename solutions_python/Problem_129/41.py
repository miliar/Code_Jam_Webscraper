#!/usr/bin/python3

from sys import stdin

def s(n):
	return n * (n + 1) // 2

def S(n, a):
	return s(n) - s(n - a)

def pay(n, _from, to):
	return S(n, to - _from)

def count(x):
	return sum([i[1] for i in x])

def solve():
	n,m = map(int, stdin.readline().split())
	g = [ tuple(map(int, stdin.readline().split())) for i in range(m) ]
	points = sorted(list(set([i[0] for i in g] + [i[1] for i in g])))
	all_cards = []
	current_cards = []
	current_passenges = 0
	enter = {i:0 for i in points}
	leave = {i:0 for i in points}
	for i in g:
		enter[i[0]] += i[2]
		leave[i[1]] += i[2]
	for point in points:
		current_passenges += enter[point] - leave[point]
		current_cards = list(reversed(sorted(current_cards)))
		if current_passenges > count(current_cards):
			current_cards.append((point, current_passenges - count(current_cards)))
		extra = count(current_cards) - current_passenges 
		while count(current_cards) > current_passenges:
			if current_cards[0][1] <= extra:
				extra -= current_cards[0][1]
				all_cards.append((current_cards[0][0], point, current_cards[0][1]))
				current_cards = current_cards[1:]
			else:
				all_cards.append((current_cards[0][0], point, extra))
				current_cards[0] = (current_cards[0][0], current_cards[0][1] - extra)
		# print('point: ', point, current_cards, all_cards, current_passenges)
	real_cost = sum([pay(n, i[0], i[1]) * i[2] for i in all_cards])
	estimated_cost = sum([pay(n, i[0], i[1]) * i[2] for i in g])
	# print(all_cards)
	# print(estimated_cost, real_cost)
	return estimated_cost - real_cost

t = int(stdin.readline())
for i in range(t):
	print('Case #%d: %d' % (i + 1, solve()))