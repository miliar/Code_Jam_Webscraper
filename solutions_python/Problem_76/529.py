#!/usr/bin/python

f1 = open("C-large.in", "r")
f2 = open("C-large.out", "w")

lines = f1.read().split("\n")

lines = lines[1:-1]

case = 0

esta = True
for line in lines:
	esta = not esta
	if esta:

		case = case + 1

		lista = map(int, line.split(" "))

		def xor(x, y): return x^y
		
		if reduce (xor, lista) != 0:
			print "Case #"+str(case)+": NO"
			f2.write("Case #"+str(case)+": NO\n")
		else:
			print "Case #"+str(case)+": "+str(sum(lista)-min(lista))
			f2.write("Case #"+str(case)+": "+str(sum(lista)-min(lista))+"\n")

f1.close()
f2.close()
