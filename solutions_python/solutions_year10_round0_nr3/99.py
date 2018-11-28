#!/usr/bin/env python3.1

import sys

def calc2(rides_remaining, capacity, queue):
	money = 0
	while rides_remaining > 0:
		cap = capacity
		queue2 = []
		while len(queue) > 0 and queue[0] <= cap:
			cap -= queue[0]
			money += queue[0]
			queue2 += [queue[0]]
			queue = queue[1:]
		queue += queue2
		rides_remaining -= 1
	return money

def calc(rides_remaining, capacity, queue):
	cycle = [0]
	queue_resets = 0
	i = 0
	while rides_remaining > 0:
		newi = doride(capacity, queue, i)
		rides_remaining -= 1
		if newi <= i: queue_resets += 1
		i = newi
		if i not in cycle:
			cycle += [i]
		else:
			cycle = cycle[cycle.index(i):]
			break
	if rides_remaining > 0:
		resets_per_cycle = resets_in(cycle + [cycle[0]])
		rides_in_cycle = len(cycle)
		cycle_count = rides_remaining // rides_in_cycle
		rides_remaining -= cycle_count * rides_in_cycle
		queue_resets += cycle_count * resets_per_cycle
		i = cycle[rides_remaining]
		queue_resets += resets_in(cycle[:rides_remaining+1])
		rides_remaining = 0
	return sum(queue) * queue_resets + sum(queue[:i])

def resets_in(rides):
	n = 0
	for i in range(1,len(rides)):
		if rides[i] <= rides[i-1]:
			n += 1
	return n

def doride(capacity, queue, i):
	startat = i
	while queue[i] <= capacity:
		capacity -= queue[i]
		i = (i + 1) % len(queue)
		if i == startat: return startat
	return i

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	args = getints()
	result = calc(args[0], args[1], getints())
	print("Case #%d: %d" % (i+1, result))
