import math
inputfile = open('A-large.in.txt')
#outputfile = open('result2.txt','w')

no_of_tests = int(inputfile.readline())


	
for casenum in range(no_of_tests):
  aa = inputfile.readline().split()
  max_shy =  long(aa[0])
  people = list(aa[1])

  res = 0
  position = 0
  no_stand = 0


  while position < len(people):
	p_at_lev = int(people[position])
	if position <= no_stand:
		no_stand=no_stand+p_at_lev
	else:
		add = position-no_stand
		res = res +add
		no_stand=no_stand+add+p_at_lev
	
	position = position +1

  print "Case #%d: %d" % (casenum+1, res)



#outputfile.close()