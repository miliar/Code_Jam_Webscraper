def isPalindrome (num):
	temp = num
	num2 = 0
	while (temp > 0):
		num2 = num2 * 10 + (temp % 10)
		temp = temp // 10
	return (num == num2)

a = [0] * 51
l = []

def iterateOdd (pos, fin, s):
	global a
	global l
	if pos == fin:
		num = 0
		for i in list(range(0,fin)):
			num = num * 10 + a[i]
		for i in list(range(fin-2,-1,-1)):
			num = num * 10 + a[i]
		if num > 0:
			l.append(num * num);
	else:
		coef = 2
		if pos == (fin-1):
			coef = 1
		r = list(range(0,4))
		if pos == 0:
			r = list(range(1,4))
		for i in r:
			if (s + coef * i * i) < 10:
				a[pos] = i
				iterateOdd(pos+1, fin, s + coef * i * i)

def iterateEven (pos, fin, s):
	global a
	global l
	if pos == fin:
		num = 0
		for i in list(range(0,fin)):
			num = num * 10 + a[i]
		for i in list(range(fin-1,-1,-1)):
			num = num * 10 + a[i]
		if num > 0:
			l.append(num * num);
	else:
		coef = 2
		r = list(range(0,4))
		if pos == 0:
			r = list(range(1,4))
		for i in r:
			if (s + coef * i * i) < 10:
				a[pos] = i
				iterateEven(pos+1, fin, s + coef * i * i)

l = []
for i in list(range(1,26)):
	iterateOdd(0,i,0)
	iterateEven(0,i,0)
l.append(10000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000001) #yep, will never be used because of limitations
l.sort() #although should be sorted already, just in case

T = int(input())
for iT in list(range(0,T)):
	lim = input().split()
	A = int(lim[0]) - 1
	B = int(lim[1])
	L = 0
	R = len(l) - 1
	while (R > L):
		C = (L+R) // 2
		if l[C] > B:
			R = C
		else:
			L = C+1
	cnt = L
	L = 0
	R = len(l) - 1
	while (R > L):
		C = (L+R) // 2
		if l[C] > A:
			R = C
		else:
			L = C+1
	cnt = cnt - L;
	print("Case #" + str(iT+1) + ": " + str(cnt))
