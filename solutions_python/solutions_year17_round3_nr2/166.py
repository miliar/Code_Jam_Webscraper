
import sys
from queue import PriorityQueue as PQue
import numpy as np
import math

sys.setrecursionlimit(1000000)

OUTPUT_FILE_NAME = "out.txt"
INF = 1e15
DX = 1e-6

out = ""



def gline():
	return input()

def gint():
	return int(gline())

def gflt():
	return float(gline())

def gstr():
	return gline()

def girow():
	return [int(x) for x in gline().split()]

def gfrow():
	return [float(x) for x in gline().split()]

def gsrow():
	return gline().split()

def gcrow():
	return list(gline())

def garr(rows, gfunc):
	arr = []
	for i in range(rows):
		arr.append(gfunc())
	return arr

def giarr(rows):
	return garr(rows, girow)

def gfarr(rows):
	return garr(rows, gfrow)

def gsarr(rows):
	return garr(rows, gsrow)

def gcarr(rows):
	return garr(rows, gcrow)


def pr(thing, separator=" "):
	
	global out
	
	if (type(thing) == list):
		for e in thing:
			if (type(e) == list):
				out += "\n"
			pr(e)
	elif (type(thing) == float):
		out += "{0:.10f}{1}".format(thing, separator)
	else:
		out += "{0}{1}".format(thing, separator)

def prc(thing):
	pr(thing, "")

def prI():
	pr("IMPOSSIBLE")


def carr(value, *dimensions):
	if len(dimensions) == 0:
		return []
	elif len(dimensions) == 1:
		return [value]*dimensions[0]
	else:
		arr = []
		e = carr(value, *dimensions[1:])
		for i in range(dimensions[0]):
			arr.append(list(e))
		return arr

def xran(start, end, *exclude):
	arr = []
	for i in range(start, end):
		if not i in exclude:
			arr.append(i)
	return arr

def xivl(a, b, *exclude):
	arr = []
	sign = np.sign(b - a)
	if sign == 0:
		arr.append(a)
	
	i = a
	while np.sign(b - i) + sign != 0:
		arr.append(i)
		i += sign
	
	return arr

def transarr(arr):
	if len(arr) == 0:
		return []
	
	newarr = carr(0, len(arr[0]), len(arr))
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			newarr[j][i] = arr[i][j]
	return newarr


def ceil(n):
	return int(math.ceil(n))

def floor(n):
	return int(math.floor(n))

def posfunc(n):
	if n > 0:
		return 1
	else:
		return 0

def negfunc(n):
	if n < 0:
		return 1
	else:
		return 0

def zerofunc(n):
	if n == 0:
		return 1
	else:
		return 0

def nposfunc(n):
	return negfunc(n) + zerofunc(n)

def nnegfunc(n):
	return posfunc(n) + zerofunc(n)

def possign(n):
	return np.sign(n) + zerofunc(n)

def neggsign(n):
	return np.sign(n) - zerofunc(n)


def cmp(left, right): #Equals sgn(right - left) if numbers.
	if left < right:
		return -1
	elif left > right:
		return 1
	else:
		return 0

def cmp_l(left, right):
	if left < right:
		return 1
	else:
		return 0

def cmp_leq(left, right):
	if left <= right:
		return 1
	else:
		return 0

def cmp_g(left, right):
	if left > right:
		return 1
	else:
		return 0

def cmp_geq(left, right):
	if left >= right:
		return 1
	else:
		return 0

def binarySearch(a, b, comp, lg=0, precision=1):
	
	if a > b:
		return None
	
	ivl = [a, b]
	
	if precision < 1:
		divfunc = lambda x, y: x/y
	else:
		divfunc = lambda x, y: x//y
	
	while ivl[1] - ivl[0] > precision:
		c = divfunc(sum(ivl), 2)
		v = comp(c)
		if v == -1:
			ivl[0] = c
		elif v == 1:
			ivl[1] = c
		elif lg == -1:
			ivl[0] = c
		elif lg == 1:
			ivl[1] = c
		else:
			return c
	
	for e in ivl[::possign(lg)]:	
		if comp(e) == 0:
			return e
	return None

def binarySearchF(a, b, func, comp, *args):
	return binarySearch(a, b, lambda x: comp(func(x)), *args)

def binarySearchFN(a, b, func, n, *args):
	return binarySearch(a, b, lambda x: cmp(func(x), n), *args)

def binarySearchA(a, b, arr, comp, *args):
	return binarySearch(a, b, lambda x: comp(arr[x]), *args)

def binarySearchAN(a, b, arr, n, *args):
	return binarySearch(a, b, lambda x: cmp(arr[x], n), *args)

def binarySearchSGN(a, b, func, n, *args):
	return binarySearch(a, b, lambda x: -cmp_leq(func(x), n), 1, *args)

def binarySearchSGEN(a, b, func, n, *args):
	return binarySearch(a, b, lambda x: -cmp_l(func(x), n), 1, *args)

def binarySearchLSN(a, b, func, n, *args):
	return binarySearch(a, b, lambda x: cmp_geq(func(x), n), -1, *args)

def binarySearchLSEN(a, b, func, n, *args):
	return binarySearch(a, b, lambda x: cmp_g(func(x), n), -1, *args)

def dSign(func, x, precision):
	return cmp(func(x + precision), func(x))

def compX(x, precision):
	return (dSign(x - precision) + dSign(x))//2

#Returns min or max of <func>, which should have exactly one extreme point on [a, b].
def binarySearchMinMaxF(a, b, func, mm, precision=1):
	
	if a > b:
		return None
	
	xpoints = [a, b]
	
	p = binarySearch(a + precision, b - precision, compX, 0, precision)
	if p != None:
		xpoints.append(p)
	
	xvalues = [(func(x), x) for x in xpoints]
	if mm == 1:
		return min(xvalues)[::-1]
	else:
		return max(xvalues)[::-1]

def binarySearchMinF(a, b, func, *args):
	return binarySearchMinMaxF(a, b, func, 1, *args)

def binarySearchMaxF(a, b, func, *args):
	return binarySearchMinMaxF(a, b, func, -1, *args)


def sumF(a, b, func):
	s = 0
	for i in range(a, b):
		s += func(i)
	return s

def isInt(x):
	return x == int(x)









def solve(tc):
	global out
	
	#Write code here:
	ac, aj = girow()
	cCD = giarr(ac)
	jCD = giarr(aj)
	
	timec = 0
	timej = 0
	total = 0
	
	CD = []
	for e in cCD:
		CD.append([e[0], e[1], 0])
		timec += e[1] - e[0]
	for e in jCD:
		CD.append([e[0], e[1], 1])
		timej += e[1] - e[0]
	CD.sort()
	
	CD.append([CD[0][0] + 1440, CD[0][1] + 1440, CD[0][2]])
	
	H = [[],[]]
	f = 0
	time2c = 0
	time2j = 0
	for i in range(len(CD) - 1):
		if CD[i][2] != CD[i + 1][2]:
			f += CD[i + 1][0] - CD[i][1]
			total += 1
		elif CD[i][2] == 0:
			time2c += CD[i + 1][0] - CD[i][1]
			H[0].append(CD[i + 1][0] - CD[i][1])
		else:
			time2j += CD[i + 1][0] - CD[i][1]
			H[1].append(CD[i + 1][0] - CD[i][1])
	H[0] = list(reversed(sorted(H[0])))
	H[1] = list(reversed(sorted(H[1])))
	
	if timec + f >= 720 and timej + f >= 720: #no extra changes needed
		pr(total)
		return
	
	if timec + f < 720:
		for h in H[1]:
			if timec + f >= 720:
				pr(total)
				return
			timec += h
			total += 2
			if timec + f >= 720:
				pr(total)
				return
	if timej + f < 720:
		for h in H[0]:
			if timej + f >= 720:
				pr(total)
				return
			timej += h
			total += 2
			if timej + f >= 720:
				pr(total)
				return
	
	








t = int(input())
for tc in range(1, t + 1):
	out += "Case #{0}: ".format(tc)
	solve(tc)
	out += "\n"
	print("Solved:", tc)


with open(OUTPUT_FILE_NAME, "w") as f:
	f.write(out)

print()
print(out)
print("\nDone.")

