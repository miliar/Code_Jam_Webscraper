#!/usr/bin/env python

import string

ipt = open("q1s.i", "r")
opt = open("q1s.o", "w+")

cases = int(ipt.readline())
print cases

f = lambda x, n: round(x, n - len(str(int(x))));

for case in range(cases) :
	print 
	args = ipt.readline().rsplit()
	A = int(args[0])
	print( "A=%d" % A )
	B = int(args[1])
	print( "B=%d" % B )

	p = ipt.readline().rsplit()
#	print( p ) 

	fact = [[],[]]
	fact[0] = [1.0, 1.0, 1.0]
	fact[1] = [1.0, 1.0, 1.0]

	for i in range(3-len(p), 3):
		fact[0][i]=float(p[i-3+len(p)])
		fact[1][i]=1-float(p[i-3+len(p)])

	prop = [ fact[0][0] * fact[0][1] * fact[0][2] ,
		 fact[0][0] * fact[0][1] * fact[1][2] ,
		 fact[0][0] * fact[1][1] * fact[0][2] ,
		 fact[0][0] * fact[1][1] * fact[1][2] ,
		 fact[1][0] * fact[0][1] * fact[0][2] ,
		 fact[1][0] * fact[0][1] * fact[1][2] ,
		 fact[1][0] * fact[1][1] * fact[0][2] ,
		 fact[1][0] * fact[1][1] * fact[1][2] ,
	       ]
	prop = [ f(fact[0][0] * fact[0][1] * fact[0][2],8) ,
		 f(fact[0][0] * fact[0][1] * fact[1][2],8) ,
		 f(fact[0][0] * fact[1][1] * fact[0][2],8) ,
		 f(fact[0][0] * fact[1][1] * fact[1][2],8) ,
		 f(fact[1][0] * fact[0][1] * fact[0][2],8) ,
		 f(fact[1][0] * fact[0][1] * fact[1][2],8) ,
		 f(fact[1][0] * fact[1][1] * fact[0][2],8) ,
		 f(fact[1][0] * fact[1][1] * fact[1][2],8) ,
	       ]

	AA = A
	BB = B

	arr1 = [   BB-AA+1,   BB-AA+1+BB+1,       BB-AA+1+BB+1,       BB-AA+1+BB+1,       BB-AA+1+BB+1,       BB-AA+1+BB+1,       BB-AA+1+BB+1,       BB-AA+1+BB+1]
	arr2 = [ 2+BB-AA+1, 2+BB-AA+1, 2+BB-AA+1+BB+1, 2+BB-AA+1+BB+1, 2+BB-AA+1+BB+1, 2+BB-AA+1+BB+1, 2+BB-AA+1+BB+1, 2+BB-AA+1+BB+1]
	arr3 = [ 4+BB-AA+1, 4+BB-AA+1,     4+BB-AA+1,     4+BB-AA+1, 4+BB-AA+1+BB+1, 4+BB-AA+1+BB+1, 4+BB-AA+1+BB+1, 4+BB-AA+1+BB+1]
	arr4 = [      BB+2,      BB+2,         BB+2,         BB+2,         BB+2,         BB+2,         BB+2,         BB+2]

	print arr1
	print arr2
	print arr3
	print arr4

	ans = 99999999.000000

	temp1 = 0.0
	temp2 = 0.0
	temp3 = 0.0
	temp4 = 0.0

	if A < 3:
		kk = A
	else:
		kk = 3

	for i in range(2**kk):
		temp1 = prop[i]*arr1[i] + temp1
		temp2 = prop[i]*arr2[i] + temp2
		temp3 = prop[i]*arr3[i] + temp3
		temp4 = prop[i]*arr4[i] + temp4

	print temp1
	print temp2
	print temp3
	print temp4

	if temp1 < ans:
		ans = temp1
	if temp2 < ans:
		ans = temp2
	if temp3 < ans:
		ans = temp3
	if temp4 < ans:
		ans = temp4

	print( "Case #%d: %f" % (case+1, ans))

	opt.write("Case #%d: %f\n" % (case+1, ans))

ipt.close()
opt.close()




