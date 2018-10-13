import sys

data = sys.stdin.read()

data = data.split("\n")
n = int(data[0])
data = list(map(lambda x:x.rstrip(), data))
for i in range(n):
	base = 1 + i*10
	c1 = int(data[base])
	pos1 = set(map(int, data[base+c1].split(" ")))
	c2 = int(data[base+5])
	pos2 = set(map(int, data[base+5+c2].split(" ")))
	res = pos1.intersection(pos2)
	if len(res) > 1:
		print("Case #{}: Bad magician!".format(i+1))
		continue
	if len(res) == 0:
		print("Case #{}: Volunteer cheated!".format(i+1))
		continue
	print("Case #{0}: {1}".format(i+1, res.pop()))
