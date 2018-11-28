import string
trans = string.maketrans("ynficwlbkuomxsevzpdrjgthaq","abcdefghijklmnopqrstuvwxyz")

f = open("A-small-attempt1.in")
lines = f.readlines()
t = lines[0]
t = int(t)
g = open("output.txt",'w')
for i in range(0,t):
	s = lines[i+1]
	s = s.translate(trans)
	s = "Case #" + str(i+1) + ": " + s
	g.write(s)
g.close()
f.close()
# h,q	# ,v
# v=g
# bz	#g
