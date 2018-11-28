import sys
import fileinput
import re

#fileio
fileName = 'A-large'
#fileName = 'A-small-attempt0'
#fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".out"
  
###
with open(input) as fi, open(output, "w") as fo:
	count = 0
	for line in fi.readlines()[1:]:
		print line
		result = 0
		arr = [0]*100
		###
		audi_list = map(lambda x: int(x), list(line.strip('\n').split(' ')[1]))
		stood = 0
		for i in range(len(audi_list)):
			a = audi_list[i]
			if stood < i: result = max(result, i-stood)
			stood += a
		###
		#normal
		count += 1
		resultStr = "Case #"+str(count)+": "+str(result)
		print resultStr
		fo.write(resultStr+'\n')

