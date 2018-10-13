
import os, sys, re, string
import math

def readint():
	return int(sys.stdin.readline())
def readints(sp=" "):
	return map(lambda x: int(x), sys.stdin.readline().split(sp))

class Plant:
	def __init__(self, v):
		self.x = v[0]
		self.y = v[1]
		self.r = v[2]

def calc(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	dd = math.sqrt(dx*dx + dy*dy)
	return (dd + p1.r + p2.r) /2

def operate():
	n = readint()
	def compile():
		return Plant(readints())
	plants = map(lambda x: compile(), range(n))
	if n == 1:
		return plants[0].r
	elif n == 2:
		return max(plants[0].r, plants[1].r)
	return min(
		max(calc(plants[0], plants[1]), plants[2].r),
		max(calc(plants[2], plants[1]), plants[0].r),
		max(calc(plants[0], plants[2]), plants[1].r),
	)

def main():
	print "\n".join(map(lambda x: "Case #%d: %3.8f" % (x, operate()), range(1, readint()+1)))

if __name__ == '__main__':
	main()

