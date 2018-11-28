#!/usr/bin/python3

import sys, os, string, re

in_file = sys.stdin
out_file = sys.stdout

debug = False
def msg(x):
	if debug:
		print(x)

class Chunker:
	def __init__(self, text, delimiter=None):
		self.chunks = text.split(delimiter)
		self.chunk_num = len(self.chunks)
		self.tick = -1
	def next(self):
		self.tick += 1
		if self.tick < self.chunk_num:
			return self.chunks[self.tick]
		return None
	def nextInt(self, how_many=0):
		if how_many:
			ints = []
			for i in range(how_many):
				ints.append(self.nextInt())
			return ints
		chunk = self.next()
		if chunk != None:
			return int(chunk)
		return None

text = in_file.read()
chunker = Chunker(text)
#line_chunker = Chunker(text, '\n')

T = int(chunker.next())
for case_num in range(1, T+1):
	out_file.write('Case #%d: ' % case_num)

	[X, S, R, t, N] = chunker.nextInt(5)

	walkways = []
	for i in range(N):
		walkways.append(chunker.nextInt(3))
	walkways.sort()

	boost = X*[0]
	for [begin, end, value] in walkways:
		for i in range(begin, end):
			boost[i] = value
	msg(boost)

	speeds = []
	for pos in range(X):
		speed = S
		speed += boost[pos]
		speeds.append(speed)
	msg(speeds)

	speeds.sort()
	turbo = t
	for (i, walk_speed) in enumerate(speeds):
		run_speed = walk_speed+R-S
		if turbo > 1/run_speed:
			speeds[i] = run_speed
			turbo -= 1/run_speed
		else:
			run_time = turbo
			run_distance = run_speed*run_time
			walk_distance = 1-run_distance
			walk_time = walk_distance/walk_speed
			speeds[i] = (run_time*run_speed + walk_time*walk_speed) /  \
					(run_time + walk_time)
			msg([run_time, run_distance, walk_time, walk_distance])
			break
	msg(speeds)

	speed_hash = {}
	for speed in speeds:
		speed_hash[speed] = speed_hash.setdefault(speed, 0)+1
	
	total = 0.0
	for (speed, count) in speed_hash.items():
		total += count/speed

	out_file.write('%.9f\n' % (total,))

