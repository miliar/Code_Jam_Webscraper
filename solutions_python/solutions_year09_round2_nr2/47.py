
import os, sys, re, string

def readint():
	return int(sys.stdin.readline())
def readints(sp=" "):
	return map(lambda x: int(x), sys.stdin.readline().split(sp))

def rare_case(inputs):
	if len(inputs) == 1:
		return True
	start = inputs[0]
	for v in inputs[1:]:
		if start < v:
			return False
		start = v
	return True
	

def operate():
	s = map(lambda x: int(x), sys.stdin.readline().strip())
	if s[0] == 0:
		for i in range(len(s)):
			if s[i] != 0:
				s[0] = s[i]
				s[i] = 0
				break
	if rare_case(s):
		s.sort()
		if s[0] == 0:
			for i in range(len(s)):
				if s[i] != 0:
					s[0] = s[i]
					s[i] = 0
					break
		return "".join(map(lambda x: str(x), [s[0], 0] + s[1:]))
	table = [0 for i in range(10)]
	for v in s:
		table[v] += 1
	length = len(s)
	def f(ary, depth, big_flag):
		if length == depth:
			return ary if ary > s else False
		minary = False
		if big_flag:
			for i in range(10):
				if table[i] > 0:
					table[i] -= 1
					res = f(ary + [i], depth + 1, True)
					table[i] += 1
					if res:
						minary = res
						break
		else:
			for i in range(10):
				if table[i] > 0 and i >= s[depth]:
					table[i] -= 1
					res = f(ary + [i], depth + 1, i > s[depth])
					table[i] += 1
					if res:
						minary= res
						break
		return minary
	return "".join(map(lambda x: str(x), f([], 0, False)))

def main():
	print "\n".join(map(lambda x: "Case #%d: %s" % (x, operate()), range(1, readint()+1)))

if __name__ == '__main__':
	main()

