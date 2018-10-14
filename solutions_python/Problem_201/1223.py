#! /usr/bin/python3
import math
import sys
sys.setrecursionlimit(10000)

# [n, n//2, n-n//2-1, ]
a = []
def fkill(n, k, n0):
	if k >= n0:
		return
	a[k-1] = n
	if n % 2 == 0:
		fkill(n//2, 2*k, n0)
		fkill(n-n//2-1, 2*k+1, n0)
	else:
		fkill(n-(n-1)//2-1, 2*k, n0)
		fkill((n-1)//2, 2*k+1, n0)

def f(n, k):
	global a
	a = [0] * n
	fkill(n, 1, n)
	a.sort(reverse=True)
	# print(a)
	k -= 1
	return a[k]//2, max(a[k] - a[k]//2 - 1, 0)

def getk(n, k):
	if k == 1:
		return n
	ni = getk(n, k // 2)
	return ni // 2
	# if k % 2 == 0:
	# 	return ni // 2
	# else:
	# 	return ni // 2
	# 	# return max(ni - (ni//2) - 1, 0)

def f2(n, k):
	ai = getk(n, k)
	return ai//2, max(ai - ai//2 - 1, 0)

def f3(n, k):
	d = n // (2 ** int(math.log(k, 2)))
	return d // 2, max(d - d // 2 - 1, 0)
	
def fkill2(n, k, n0, k0):
	if k >= k0:
		return [n]
	# a[k-1] = n
	if n % 2 == 0:
		a1 = fkill2(n//2, 2*k, n0, k0)
		a2 = fkill2(n-n//2-1, 2*k+1, n0, k0)
	else:
		a1 = fkill2(n-(n-1)//2-1, 2*k, n0, k0)
		a2 = fkill2((n-1)//2, 2*k+1, n0, k0)
	a = sorted(a1 + a2, reverse=True)
	print('a', a)
	return a

def f4(n, k):
	a = fkill2(n, 1, n, k)
	# a.sort(reverse=True)
	print(a)
	k -= 1
	return a[k]//2, max(a[k] - a[k]//2 - 1, 0)

t = int(input())
for it in range(1, t+1):
	n, k = map(int, input().split())
	# print(n, k)
	o1 = f(n, k)
	# o2 = f2(n, k)
	# o3 = f3(n, k)
	# o4 = f4(n, k)
	# assert o1 == o4, (n, k, o1, o4)
	print("Case #%d:" % it, *o1)
