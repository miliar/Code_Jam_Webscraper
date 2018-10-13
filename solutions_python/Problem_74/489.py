#!/usr/bin/python

import sys
rl = sys.stdin.readline

if __name__ == '__main__':
	tests = int(rl())

	for case in xrange(1, tests + 1):
		bots, last, result = {}, {}, 0
		data = rl().split()
		sequence, previous = zip(data[1::2], map(int, data[2::2])), None

		for bot, hallway in sequence:
			current = bots.get(bot, 1)
			moves = abs(current - hallway)
			bots.update({bot: hallway})

			if all([previous, bot != previous, moves]):
				result = max(last.get(bot, 0) + moves, result)
			else:
				result += moves

			result += 1
			last.update({bot: result})
			previous = bot

		print 'Case #%d: %d' % (case, result)

