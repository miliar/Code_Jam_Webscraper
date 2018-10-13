#!/usr/bin/python3

# Hmmm... easier to verify than to solve... is writing a solution verifier the fastest way to get going?
# Easy case is solve within 500 moves... 4 possible states is 4^500... too huge to bruteforce
# Obvious solution is to bounce along to X, then to Y... but there will probably have to be sort of interchange between
# them
# And each number can be selected to go +ve or -ve... and every one has to be used
# HRMMMM, the dumb solution is to use pairs of numbers to make 1-by-1 adjustments one it gets closer
# Divide the first few steps into approaching, then just dial it in... I guess
# +6-5 = +1

# Stupid solution for small... definitely not the shortest path!
cases = int(input())

def debug(*args):
	#print(*args)
	pass

def verify(path):
	counter = 1
	x = y = 0
	for c in path:
		if c == 'N':
			y += counter
		elif c == 'S':
			y -= counter
		elif c == 'E':
			x += counter
		elif c == 'W':
			x -= counter
		else:
			print("WTF???")
		counter += 1
	return (x, y)

for case in range(1, cases+1):
	x, y = map(int, input().split())
	ox = x
	oy = y
	invert_x = False
	invert_y = False
	path = ""
	if x < 0:
		invert_x = True
		x *= -1
	if y < 0:
		invert_y = True
		y *= -1
	
	cx = cy = 0
	
	counter = 1
	while cx < x:
		cx += counter
		counter += 1
		path += "E"
	debug("Stopped at %s with %s" % (cx, path))
	
	diff = cx - x
	path += "EW" * diff
	counter += diff*2

	while cy < y:
		cy += counter
		counter += 1
		path += "N"
	debug("Stopped at %s with %s" % (cy, path))
	diff = cy - y
	debug("Adding %s blocks from %s" % (diff, verify(path)))
	for x in range(diff):
		path += "NS"
		debug("%s %s" % (path, verify(path)))
	#path += "NS" * diff
	counter += diff*2

	if invert_x:
		path = path.replace("E", "X")
		path = path.replace("W", "E")
		path = path.replace("X", "W")
	if invert_y:
		path = path.replace("N", "X")
		path = path.replace("S", "N")
		path = path.replace("X", "S")

	debug(path)
	(nx, ny) = verify(path)
	debug(verify(path))
	debug("%s %s" % (ox, oy))
	if nx != ox or ny != oy:
		print("WRONG!!!!!!")
	

	if len(path) > 500:
		print("Solution too long!")

	print("Case #%s: %s" % (case, path))

