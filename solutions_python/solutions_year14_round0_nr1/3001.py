f1=file("./outA.out","w+")
t = int(input())
for i in range(1,t+1):
	r1 = int(input())
	aux = []
	for j in range(1,5):
		s = raw_input().split(" ")
		if j == r1:
			aux = s
	r2 = int(input())
	aux2 = []
	for j in range(1,5):
		s = raw_input().split(" ")
		if j == r2:
			aux2 = s
	res = set(aux2).intersection(set(aux))
	if len(res) == 1:
		print >> f1,"Case #%d: %s" % (i,list(res)[0])
	if len(res) >1:
		print >> f1,"Case #%d: Bad magician!" % i
	if len(res) == 0:
		print >> f1,"Case #%d: Volunteer cheated!" % i
