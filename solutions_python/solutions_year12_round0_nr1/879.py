import sys

l1 = "abcdefghijklmnopqrstuvwxyz"
l2 = "yhesocvxduiglbkrztnwjpfmaq"

def trans(c):
	i = l1.find(c)
	if i >= 0: return l2[i]
	if c == '\n': return "";
	return c
	

x = sys.stdin.readline()
x = int(x)
i = 1
while i <= x:
	input = sys.stdin.readline()
	out = ""
	for c in input:
		out += trans(c)
	print("Case #%d: %s" % (i, out)) 
	i += 1