inp = open("inputL.txt", 'r')

tests =int( inp.readline())

for i in range(tests):
	p = inp.readline().split()
	cost =float( p[0])
	farm =float( p[1])
	obj = float(p[2])
	pro =2
	time=0
	while 1:
		if obj/pro < (obj/(pro+farm)+cost/pro):
			time += obj/pro
			break
		else:
			time += cost/pro
			pro += farm
	print("Case #",i+1,": ", time, sep="")
