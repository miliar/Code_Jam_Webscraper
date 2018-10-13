#!/usr/bin/env python3

from collections import Counter
import math
from collections import defaultdict

for L in range(int(input())):
	R,C = map(int, input().split())
	maze = []
	for _ in range(R):
		maze.append(list(input()))
	#original lazer orientation is irrelevant
	
	#tiles: / \ - | # .
	
	#returns tiles hit until # or OOB
	#d = 0=right, 1=up, 2=left, 3=down
	def fire(p,d):
		(y,x) = p
		while True:
			try:
				if d==0: x+=1
				if d==1: y-=1
				if d==2: x-=1
				if d==3: y+=1
				if y<0 or x<0: break
				tile = maze[y][x]
				
				if tile=='.': yield (y,x)
				if tile=='#': break
				if tile=='-':
					yield (-1,-1)
					break
				if tile=='|':
					yield (-1,-1)
					break
				if tile=='/': d = [1,0,3,2][d]
				if tile=='\\':d = [3,2,1,0][d]
			
			except IndexError:
				break
	
	doable = "POSSIBLE"
	#every . is in here, keyed by tuple (Y,X)
	#value is array of ((1,2),'-'), which lazers target this tile and which direction (the lazer can appear twice in both directions)
	target = defaultdict(list)
	#keyed by tuple (Y,X), value is "-|", "-" or "|"
	lazers = {}
	
	for y in range(R):
		for x in range(C):
			if maze[y][x]=='-' or maze[y][x]=='|':
				lazers[(y,x)] = "-|"
				#print(y,x,0,list(fire((y,x), 0)))
				#print(y,x,1,list(fire((y,x), 1)))
				#print(y,x,2,list(fire((y,x), 2)))
				#print(y,x,3,list(fire((y,x), 3)))
				for yh,xh in fire((y,x), 0): target[(yh,xh)].append(((y,x),'-'))
				for yh,xh in fire((y,x), 1): target[(yh,xh)].append(((y,x),'|'))
				for yh,xh in fire((y,x), 2): target[(yh,xh)].append(((y,x),'-'))
				for yh,xh in fire((y,x), 3): target[(yh,xh)].append(((y,x),'|'))
			if maze[y][x]=='.':
				len(target[(y,x)]) # just reference it
	
	#p=tuple, d='-' or '|'
	def ban_dir(p,d):
		if d=='-' and lazers[p]=="-|":
			lazers[p] = "|"
			return True
		if d=='|' and lazers[p]=="-|":
			lazers[p] = "-"
			return True
		if d=='-' and lazers[p]=="-":
			1/0
		if d=='|' and lazers[p]=="|":
			1/0
		return False
	
	def require_dir(p,d):
		if d=='-': ban_dir(p,'|')
		if d=='|': ban_dir(p,'-')
	
	#like target, but no key, just a set of 'at least one of these must be true'
	constraints = []
	#remove coordinates from targets
	for coord in target:
		if coord == (-1,-1):
			for p,d in target[coord]:
				try:
					ban_dir(p,d)
				except ZeroDivisionError:
					doable = "IMPOSSIBLE"
		else:
			constraints.append(target[coord])
	
	def dfs(constraints, lazers):
		while True:
			action = False
			for i,con in enumerate(constraints):
				#nuke impossibilities
				con = [(p,d) for p,d in con if d in lazers[p]]
				if len(con) != len(constraints[i]):
					action = True
				constraints[i] = con
				if len(con)==0:
					1/0
				if len(con)==1:
					require_dir(con[0][0], con[0][1])
					action = True
			constraints = [con for con in constraints if len(con)>1]
			
			if not action:
				for p in lazers:
					if lazers[p]=='-|':
						new_lazers = dict(lazers)
						try:
							new_lazers[p] = '-'
							return dfs(list(constraints), new_lazers)
						except ZeroDivisionError:
							new_lazers[p] = '|'
							return dfs(list(constraints), new_lazers)
				
				return lazers
	
	if doable != "IMPOSSIBLE":
		try:
			lazers = dfs(constraints,lazers)
		except ZeroDivisionError:
			doable = "IMPOSSIBLE"
	
	#print(maze)
	
	#print(target)
	#print(constraints)
	#print(lazers)
	
	#while True:
	#	for coord in target:
	#		if coord == (-1,-1):
	#			for p,d in target[coord]:
	#				ban_dir(p,d)
	#		print(coord)
	#	break
	
	print("Case #"+str(L+1)+":", doable)
	if doable!="IMPOSSIBLE":
		for y,x in lazers:
			maze[y][x] = lazers[(y,x)]
		for line in maze: print(''.join(line))
