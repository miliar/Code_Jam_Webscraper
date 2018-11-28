#!/usr/bin/env python
import string

ipt = open("q1l.i", "r")
opt = open("q1l.o", "w+")

cases = int(ipt.readline())
#print cases
Xwon = {'X', 'T'}
Owon = {'O', 'T'}
dot = {'.'}
NC = False
Winner = ''

for case in range(cases) :
	NC = False
	Winner = ''
	args = []
	case=case+1
#	print case
	for cnt in range(4) :
		args.append(list(ipt.readline().rstrip()))
#	print args
	arg2 = map(list, zip(*args))
#	print arg2
	ipt.readline()
	arg3 = [args[0][0], args[1][1], args[2][2], args[3][3]]
	arg4 = [args[3][0], args[2][1], args[1][2], args[0][3]]

	s1 = set(arg3)
	s2 = set(arg4)
#	print s1
#	print s2
	if s1.issubset(Xwon) or s2.issubset(Xwon) : 
		Winner = 'X'
	if s1.issubset(Owon) or s2.issubset(Owon) : 
		Winner = 'O'

	for cnt in range(4) :
		if Winner != '' : break
		aa = set(args[cnt])
		bb = set(arg2[cnt])
		if aa.issubset(Xwon) or bb.issubset(Xwon) : 
			Winner = 'X'
		if aa.issubset(Owon) or bb.issubset(Owon) : 
			Winner = 'O'
		if aa.issuperset(dot) : NC = True

	if Winner != '' :
		print "Case #%i: %s won" % (case,Winner)
		opt.write("Case #%i: %s won\n" % (case,Winner))
	else :
		if NC == True :
			print "Case #%i: Game has not completed" % (case)
			opt.write("Case #%i: Game has not completed\n" % (case))
		else :	
			print "Case #%i: Draw" % (case)
			opt.write("Case #%i: Draw\n" % (case))

ipt.close()
opt.close()

