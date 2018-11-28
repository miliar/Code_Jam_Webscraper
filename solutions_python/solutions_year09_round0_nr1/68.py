import re
import string
params= raw_input()
params=params.split(' ')
L=int(params[0])
D=int(params[1])
N=int(params[2])
i=0
words=''
while i<D:
	words+=raw_input()+'\r\n'
	i+=1
i=0
while i<N:
	testcase=raw_input()
	testcase=testcase.replace('(','[')
	testcase=testcase.replace(')',']')
	ret=re.findall(testcase,words)
	i+=1
	print "Case #"+str(i)+": "+str(len(ret))
	