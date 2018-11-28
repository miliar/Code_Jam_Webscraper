import sys


class tidy():
	stringArray = []
	def startProcessing(self,caseNumber,number):
		
		while number > 0:
			self.stringArray = []
			if number < 10:
				print 'Case #'+str(caseNumber)+': '+str(number)
				return
			else:
				stringNumb = str(number)
				for i in stringNumb:
					self.stringArray.append(i)
				
				count = 0
				flag = 0
				while count < len(self.stringArray)-1:
					if int(self.stringArray[count])<=int(self.stringArray[count+1]):
						count += 1
					else:
						count = len(self.stringArray)
						number = number -1
						flag = 1
				if flag == 0:
					print 'Case #'+str(caseNumber)+': '+str(number)
					return

						
		

if __name__=="__main__":
	t = tidy()
	testCases = 1
	with open('/Users/saavn/Downloads/B-small-attempt0.in.txt','rb') as fptr:
		fptr.next()
		for row in fptr:
			number = int(row)
			t.startProcessing(testCases,number)
			testCases +=1