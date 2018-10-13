#!/usr/bin/python3

from collections import defaultdict

def debug(*args):
	#print(*args)
	pass


cases = int(input())
for case in range(1, cases+1):
	numtribes = int(input())
	tribes = []
	#[0] first attack
	#[1] number of attacks
	#[2] eastmost edge
	#[3] westmost edge
	#[4] initial strength
	#[5] attack interval (time)
	#[6] moving distance to next attack
	#[7] change in strength to next attack

	# Values get rewritten to reflect current status

	for x in range(numtribes):
		tribes.append(list(map(int, input().split())))
	
	wall = defaultdict(int) # Unbounded, so dict is easier
	wall2 = wall.copy()

	def next_attack():
		# There's probably a faster, more python-ish way to do this...
		best = (-1, 10e7)
		for i, t in enumerate(tribes):
			if t[1] > 0 and t[0] < best[1]:
				best = (i, t[0])
		return best

	date = 0
	event = next_attack()
	s_attacks = 0

	def attack(left, right, strength):
		successful = 0
		# Argh, double stuff to get the stupid in-between points
		# attack [0,2] and [3,5]
		# There should still be a 0 point in the middle
		# so array should be
		# 0: 10 1(0.5): 10 2(1.0) 10 3(1.5) 10 4(2.0) 10 5(2.5): _0_ 6(3.0): 8
		for x in range(left*2, right*2 + 1):
			if wall[x] < strength:
				successful = 1
			wall2[x] = max(wall2[x], strength)
		debug(wall)
		return successful


	while event[0] > -1:
		debug("\n")
		debug(event)
		tribe = tribes[event[0]]
		debug(tribe)
		debug("Attacks from %s to %s" % (tribe[2], tribe[3]))

		if tribe[0] > date:
			wall = wall2
			wall2 = wall.copy()
			date = tribe[0]

		if attack(tribe[2], tribe[3], tribe[4]):
			s_attacks += 1
			debug("SUCCESS")

		tribe[1] -= 1
		if tribe[1] < 1:
			tribe[0] = -1
		else:
			tribe[0] += tribe[5]
			tribe[2] += tribe[6]
			tribe[3] += tribe[6]
			tribe[4] += tribe[7]
		tribes[event[0]] = tribe

		event = next_attack()
	debug(wall)

	print("Case #%s: %s" % (case, s_attacks))

