#!/usr/bin/env python3


def good(limit=10**7, str=str, reversed=reversed, int=int):
	def pals():
		for i in range(1,limit+1):
			a, b = i, 0
			while a:
				b = a % 10 + b * 10
				a //= 10
			if b == i:
				yield i
	for i in pals():
		sq = i*i
		a, b = sq, 0
		while a:
			b = a % 10 + b * 10
			a //= 10
		if b == sq:
			yield sq

#for ok in good(10**50): print(ok)
#print("ok")

#print(list(good(10**7)))
good = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

t = int(input())
for test in range(1, t+1):
	a, b = map(int, input().split())
	l = list(filter(lambda x: a<=x<=b, good))
	print("Case #%d: %d" % (test, len(l)))