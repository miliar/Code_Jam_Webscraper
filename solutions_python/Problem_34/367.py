import sys
import re

input = open(sys.argv[1], 'r')

header = input.readline()
[l,d,n] = header.split(" ");
dict=[]
tests=[]

for i in range(0,int(d)):
	dict.append(""+input.readline())
for i in range(0,int(n)):
	tests.append(""+input.readline())

testno=0
for test in tests:
	testno=testno+1
	test=test.replace('(', '[')
	test=test.replace(')', ']')

	parse = re.compile(test)
	counter = 0
	for word in dict:
		if re.match(test,word):
			counter=counter+1
	print "Case #"+str(testno)+":",counter
			
	
