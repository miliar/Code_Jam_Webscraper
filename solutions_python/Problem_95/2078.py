inf = open("input")
ouf = open("output")
ins = inf.read()
out = ouf.read()

z = dict()

v = set()

for i in range(0, len(ins)):
	if 'a' <= ins[i] and ins[i] <= 'z':
		z[ins[i]] = out[i]
		v.add(out[i])

for i in range(0, 26):
	b = chr(ord('a') + i)
	if b not in v:
		miss = b

for i in range(0, 26):
	b = chr(ord('a') + i)
	if b in z:
		print(b, ' ', z[b])
	else:
		print(b, ' ', miss)
		z[b] = miss

test = open("A-small-attempt0.in")
ans = open("A-small-attempt0.out", "w")

n = int(test.readline())
data = test.read().split("\n")

case = 0
for s in data:
	case = case + 1
	if case > n:
		break
	ans.write("Case #" + str(case) + ": ")	
	for i in range(0, len(s)):
		if 'a' <= s[i] and s[i] <= 'z':
			ans.write(z[s[i]])
		else:
			ans.write(s[i])
	ans.write("\n")
ans.close()
		