import math

f = open("C.txt", 'w')

def ispalin(k):
	k = str(k)
	if (k == k[::-1]):
		return True
	return False

def answer(a, b):
	c = 0
	k = int(math.sqrt(a))
	if (k*k < a):
		k += 1
	while (k*k <= b):
		if (ispalin(k) and ispalin(k*k)):
			c += 1
			#f.write(str(k))
			#f.write(' ')
			#f.write(str(k*k))
			#f.write('\n')
		k += 1
	return c

t = int(raw_input())
ans = []
for i in range(0, t):
	r = map(int, raw_input().split())
	ans.append(answer(r[0], r[1]))

for i in range(0, t):
	f.write("Case #")
	f.write(str(i+1))
	f.write(": ")
	f.write(str(ans[i]))
	f.write('\n')