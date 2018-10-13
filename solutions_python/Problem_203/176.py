from itertools import *
from pprint import pprint

def valid(cake):
	cake = [c[:] for c in cake]
	seen = ""
	for x in range(len(cake)):
		for y in range(len(cake[0])):
			if cake[x][y] == '?':
				1/0
			elif cake[x][y] == '_':
				continue
			elif cake[x][y] in seen:
				return False
			letter = cake[x][y]
			seen += letter
			for x2 in range(x, len(cake)+1):
				if x2 == len(cake):
					break
				if cake[x][y] != cake[x2][y]:
					break
			for y2 in range(y, len(cake[0])+1):
				if y2 == len(cake[0]):
					break
				if cake[x][y] != cake[x][y2]:
					break
			for x3 in range(x, x2):
				for y3 in range(y, y2):
					if cake[x3][y3] != letter:
						return False
					cake[x3][y3] = '_'
	return True


def solve(cake):
	letters = ""
	unk = []
	for x in range(len(cake)):
		for y in range(len(cake[0])):
			if cake[x][y] == "?":
				unk.append((x,y))
			else:
				letters += cake[x][y]
	for attempt in product(letters, repeat=len(unk)):
		for a,b in zip(unk, attempt):
			cake[a[0]][a[1]] = b
		if valid(cake):
			return cake
	return [["WTF"]]

T = int(input())
for case in range(T):
	R,C = map(int, input().split())
	cake = []
	for row in range(R):
		cake.append(list(input()))
	print("Case #{}:".format(case+1))
	print("\n".join("".join(c) for c in solve(cake)))
