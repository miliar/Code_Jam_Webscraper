from itertools import islice
import collections
import sys

fout = open(sys.argv[2],'w')

with open(sys.argv[1],'r') as f:
    	numTests = int(f.readline())
	#print numTests
	#print '-------------------'
	testNum = 0

	while True:
		testNum += 1
        	next_n_lines = list(islice(f, 10))
        	if not next_n_lines:
            		break
		answer1 = int(next_n_lines[0])
		answer2 = int(next_n_lines[5])
		#print answer1
		#print answer2
		#print '***************'
		row1 = next_n_lines[answer1].rstrip()
		#print row1
		row2 = next_n_lines[answer2 + 5].rstrip()
		#print row2
		#print '***************'
		mergedrows = row1.split(' ') + row2.split(' ')
		#print mergedrows
		#print '***************'
		duplicates = [x for x, y in collections.Counter(mergedrows).items() if y > 1] 
		duplicatecount  = len(duplicates)		
		#print duplicatecount
		if duplicatecount == 0:
			result =  'Case #' + str(testNum) + ': Volunteer cheated!'
		elif duplicatecount == 1:
			result = 'Case #' + str(testNum) + ': ' + str(duplicates[0])
		elif duplicatecount > 1:
			result = 'Case #' + str(testNum) + ': Bad magician!'
		

		print result
		fout.write(result + '\n')
		#print '+++++++++++++++++++'
      		#for line in next_n_lines:
		#	print line
		#print '--------------------'

fout.close()
#print 'fin!'

