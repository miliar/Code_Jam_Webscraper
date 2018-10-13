input = open("Expensive Dinner.in")
output = open("Expensive Dinner.out", "w")
T = int(input.readline())

N = []
result = []
M = 0
for t in range(T):
	n = int(input.readline())
	N.append(n)
	M = max(M, n)
	result.append(0 if n == 1 else 1)

S = []
R = [1]
for i in range(1, M + 1):
	if i not in R:
		a = i
		while True:
			a *= i
			for j in range(T):
				if a <= N[j]:
					if j == 3:
						print(a)
					result[j] += 1
			if a > M:
				break
		a = i
		while True:
			a += i
			if a > M:
				break
			R.append(a)

#for t in range(T):
#	for i in S:
#		if i < result[

for t in range(T):
	print("Case #{case}: {result}".format(case = t + 1, result = result[t]), file = output)
