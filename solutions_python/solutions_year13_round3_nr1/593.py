
import re
vowel = ['a', 'e', 'o', 'u', 'i'] 
ntest = int(raw_input())
for itc in range(ntest):
  print 'Case #%d:' % (itc+1),
  word, n =  raw_input().split()
  n = (int)(n)
  # print word
 
  temp = word
  count = 0

  for j in xrange(len(temp) -n + 1): 
	for i in xrange(len(temp) - n + 1): 
		val = temp[:n+i] 
	#	print "all %s" % val
		flag = True
		reg = "[^aeiou]{%d,}" % n

		exp = re.compile(reg)
		if re.search(exp, val): 
#			print val
			count = count +1 
	temp = temp[1:] 
  print count


  
