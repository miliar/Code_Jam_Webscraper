#! /usr/bin/python
import sys
def flip(ch, pos, size):
	for i in range(pos, pos+size):
		if ch[i] == "+":
			ch[i] = "-"
		else:
			ch[i] = "+"
	return ch

def stop(ch):
	i = 0
	while i < len(ch):
		if ch[i] == "-":
			return 1
		i += 1
	return 0

def smile(ch, size):
	i = 0
	j = 0
	while stop(ch):
		if ch[i] == "+":
			i += 1
		else:
			ch = flip(ch, i, size)
			j += 1
		if i > len(ch)-size:
			break
	if stop(ch) == 0:
		return j
	else:
		return -1

f_i = open(sys.argv[1], "r")
f_o = open("output.out", "w")
T = int(f_i.readline())
print T
for i in range(T):
	l = f_i.readline()
	l = l[:-1]
	l = l.split()
	if len(l) != 2:
		break
	size = int(l[1])
	ch = list(l[0])
	x = smile(ch, size)
	if x == -1:
		out = "Case #"+str(i+1)+": IMPOSSIBLE"
	else:
		out = "Case #"+str(i+1)+": "+ str(x)
	f_o.write(out+"\n")
	print out ,l[0]


f_i.close()
f_o.close()
