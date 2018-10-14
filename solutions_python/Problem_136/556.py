inp = open("B-large.in", "r")
#inp = open("input.txt", "r")
R=lambda:map(float, inp.readline().strip().split(' '))
f = open("output.txt", "w")

def decide(c, t, x, pre):
	if x / (pre) > (c / pre + x / (pre + t)):
		return 1, c / pre
	else:
		return 0, x / pre

T = int(R()[0])

cnt = 0
while cnt < T:
	cnt += 1
	c,t,x = R()

	ret = 0.0
	pre = 2
	while True:
		flag, cost = decide(c,t,x,pre)
		ret += cost
		if flag == 1:
			pre += t
		else:
			break

	f.write("Case #%d: %.7f\n" % (cnt, ret))