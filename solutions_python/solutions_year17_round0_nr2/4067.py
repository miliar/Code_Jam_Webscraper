
import sys

#1000001
#1011000
#2888887
#27999990
#833330

if __name__ == "__main__":

	filename = sys.argv[1]
	with open(filename) as f: 
		content = f.readlines()
		content = [x.strip() for x in content] 

	argcount = int(content[0])


	for count in xrange(1, argcount+1, 1):
		#print "Line Number:", count 
		number = int(content[count])


		#print number

		if number < 10: 
			#print "Tidy Number"
			a = number 
		else: 
			numstr = str(number)
			digits = len(numstr)
			flag = True
			culprit = 100000
			answer = []

			for l in xrange(digits):
				answer.append("0")

			for i in xrange(digits-1): 
				if numstr[i] > numstr[i+1]: 
					if i == 0:
						culprit = 0	
						#print culprit
						break
					else:
						for j in xrange(i-1, -1, -1):
							#print j
							if numstr[j] != numstr[j+1]: 
								flag = False
								culprit = j+1
						if flag == True:
							culprit = 0
						#print culprit
						break
			#print "Culprit", culprit

			if culprit == 100000: 
				a = number
				print "Case #%s: %s" % (count, a)
				continue
			for h in xrange(culprit): 
				answer[h] = numstr[h]
			answer[culprit] = int(numstr[culprit])-1
			for k in xrange(culprit+1, digits, 1):
				answer[k] = '9' 

			a = map(str, answer)
			a = ''.join(a)
			a = int(a)
			#print a

		print "Case #%s: %s" % (count, a)




				

		
