#!/usr/bin/python

f1 = open("A-small.in", "r")
f2 = open("A-small.out", "w")

lines = f1.read().split("\n")

lines = lines[1:-1]

case = 0

for line in lines:
	case = case + 1
	io = 1
	ib = 1
	acumo=0
	acumb=0
	line = line[2:].split(" ")
	for x in line:
		if x=='O':
			o = True
		if x=='B':
			o = False
		if x.isdigit():
			x=int(x)
			if o:
				acumo = acumo + abs(io-x)
				io = x
				if acumo < acumb:
					acumo = acumo + abs(acumo-acumb)
				acumo = acumo + 1
			else:
				acumb = acumb + abs(ib-x)
				ib = x
				if acumo > acumb:
					acumb = acumb + abs(acumb-acumo)
				acumb = acumb + 1
	if acumb > acumo:
		f2.write("Case #"+str(case)+": "+str(acumb)+"\n")
	else:
		f2.write("Case #"+str(case)+": "+str(acumo)+"\n")

f1.close()
f2.close()
