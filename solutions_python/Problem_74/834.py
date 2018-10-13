#!/usr/bin/env python
import string

ipt = open("q1l.i", "r")
opt = open("q1l.o", "w+")

case = ipt.readline()
case = 0

for line in ipt:
#	print line
	case=case+1
	line.strip()
	item =  line.rsplit(" ")
	pos = { 'O':1, 'B':1 }
	O=1
	B=1
	count = 0
	btns = item[0]
#	print btns
	probot = item[1]
	pcount = 0
	secs = 0
        for i in range(int(btns)):
#		print("%c,%d" % (item[1+i*2], int(item[1+i*2+1])))
		if probot == item[1+i*2] :
			pcount += abs(int(item[1+i*2+1])-pos[item[1+i*2]])+1
			secs += abs(int(item[1+i*2+1])-pos[item[1+i*2]])+1
			pos[item[1+i*2]] = int(item[1+i*2+1])
		else :
			probot = item[1+i*2]
			if abs(int(item[1+i*2+1])-pos[item[1+i*2]]) > pcount :
				secs += abs(int(item[1+i*2+1])-pos[item[1+i*2]]) - pcount + 1
				pcount = abs(int(item[1+i*2+1])-pos[item[1+i*2]]) - pcount + 1
				pos[item[1+i*2]] = int(item[1+i*2+1])
			else :
				secs += 1
				pcount = 1
				pos[item[1+i*2]] = int(item[1+i*2+1])
#		print pcount
#		print secs
#		print pos

	print secs
	opt.write("Case #%d: %d\n" % (case, secs))

ipt.close()
opt.close()




