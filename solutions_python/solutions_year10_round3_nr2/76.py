import sys, os

filename = "B-large"
#filename = "test"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

T = int(reader.readline().rstrip())

caseno = 1
while caseno<=T:
	L,P,C = [int(x) for x in reader.readline().rstrip().split(' ')]
	
	print (L,P,C)
	t = L*C
	cnt = 0
	while t<P:
		cnt += 1
		t = t*C
	#print cnt
	k = 0
	while cnt>0:
		cnt = cnt/2
		k += 1
	print k
	writer.write("Case #%s: %d\n" % (str(caseno),k))
	caseno+=1

writer.close()