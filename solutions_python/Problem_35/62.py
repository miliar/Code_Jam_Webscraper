#!/usr/bin/env python
#
#       jam.py
#
#       Copyright 2009 Denis <denis@denis-desktop>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import re

table = []
w = 0
h = 0

def main():
	global table, h, w

	with open("in") as f:
		maps = f.readline().strip()
		maps = int(maps)

		for case in xrange(1, maps+1):
			h, w = f.readline().strip().split(' ')
			h = int(h)
			w = int(w)
			table = []
			for row in xrange(0, h):
				table.append(map(int, f.readline().strip().split(' ')))

			dirs = []
			basin = []
			answer = []
			for row in range(0, h):
				dirs.append([])
				basin.append([])
				answer.append([])
				for col in range(0, w):
					dirs[row].append(checkCell(row,col))
					basin[row].append(0)
					answer[row].append('')

			basinNo = 1
			morebasins = True
			while morebasins:
				target = {
					'row': -1,
					'alt': 10000
				}
				for row in xrange(0, h):
					for col in xrange(0, w):
						if basin[row][col] == 0 and table[row][col] < target['alt']:
							target['col'] = col
							target['row'] = row
							target['alt'] = table[row][col]
				if target['row'] == -1:
					morebasins = False
				else:
					# sink
					basin[target['row']][target['col']] = basinNo

					queue = [(target['row'], target['col'])]

					while queue:
						row, col = queue.pop()
						#top
						if row > 0 and dirs[row-1][col] == 'S':
							basin[row-1][col] = basinNo
							queue.append((row-1,col))
						#left
						if col > 0 and dirs[row][col-1] == 'E':
							basin[row][col-1] = basinNo
							queue.append((row,col-1))
						#right
						if col < w-1 and dirs[row][col+1] == 'W':
							basin[row][col+1] = basinNo
							queue.append((row,col+1))
						#bottom
						if row < h-1 and dirs[row+1][col] == 'N':
							basin[row+1][col] = basinNo
							queue.append((row+1,col))

					basinNo += 1


			vocabulary = {}
			letterNo = ord('a')-1
			for row in xrange(0,h):
				for col in xrange(0,w):
					if basin[row][col] in vocabulary:
						answer[row][col] = vocabulary[basin[row][col]]
					else:
						letterNo += 1
						vocabulary[basin[row][col]] = chr(letterNo)
						answer[row][col] = vocabulary[basin[row][col]]

			print "Case #%d:" % (case)
			print "\n".join(map(' '.join, answer))
	return 0

def checkCell(row, col):
	global table, h, w

	def checkValue(row, col, dir):
		if table[row][col] < min['alt'] and table[row][col] < val:
			min['dir'] = dir
			min['alt'] = table[row][col]

	val = table[row][col]
	min = {
		'dir': 'NA',
		'alt': 10000
	}
	if (row > 0):
		checkValue(row-1, col, 'N')
	if (col > 0):
		checkValue(row, col-1, 'W')
	if (col < w-1):
		checkValue(row, col+1, 'E')
	if (row < h-1):
		checkValue(row+1, col, 'S')
	return min['dir']

if __name__ == '__main__': main()
