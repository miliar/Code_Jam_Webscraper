f = open('input', 'r')
ff = open('output', 'w')

f.read()

nline = 0
lines = [line.strip() for line in open('A-small-attempt2.in')]


input = lines;



for x in range(0,int(input[0])):
	sel1 = int(input[(1)+(x*10)])
	iline1 = input[sel1+1+(x*10)]
	sel2 = int(input[(6)+(x*10)])
	iline2 = input[sel2+1+5+(x*10)]
	count = 0

	arrline1 = iline1.split(' ')
	arrline2 = iline2.split(' ')
	b=0

	count=0
	for y in range(0,4):
		for z in range(0,4):
			if arrline1[y]==arrline2[z]:
				count+=1
				b=arrline1[y]	
				break
	if count == 1:
		txt = ("Case #%d: %d" % ((x+1),int(b)))
	elif count > 1:
		txt = ("Case #%d: Bad magician!" % (x+1))
	elif count == 0:
		txt =("Case #%d: Volunteer cheated!" % (x+1))
	else :
		txt = ("error :(")
	ff.write(txt+"\n")

ff.close()