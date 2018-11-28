def invcut(r,k):
	prefix = ""
	for c in r[:k]:
		if c == "+":
			prefix = prefix + "-"
		else:
			prefix = prefix + "+"
	return prefix[1:] + r[k:]
		


def getmin(r,k):
	res = 0
	while True:
		if len(r) < k:
			try:
				r.index("-")
				return "IMPOSSIBLE"
			except ValueError:
				break
		elif len(r) == k:
			if ("+"*k) == r:
				break
			elif ("-"*k) == r:
				res += 1
				break
			else:
				return "IMPOSSIBLE"
		else:
			if r[0] == "+":
				r = r[1:]
			else:
				r = invcut(r,k)
				res += 1
	return res

T = int(input())

for _ in range(0,T):
	S, K = input().split(" ")
	K = int(K)
	try:
		print("Case #{}: {}".format(_+1,getmin(S,K)))
	except ValueError:
		print("Case #{}: {}".format(_+1,"IMPOSSIBLE"))


