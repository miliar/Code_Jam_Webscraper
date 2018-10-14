import sys

class InputReader:
	def __init__(self,filePath):
		try:
			f = open(filePath)
			contents = f.readlines()
			f.close()
			N = contents.pop(0)
			with open('output.out','w') as fout:
				count = 1
				while len(contents) > 0:
					print '\n**************\n'
					print len(contents)
					a1 = contents.pop(0)
					A1 = []
					for i in range(4):
						A1.append([int(j) for j in contents.pop(0).split(' ')])
					a2 = contents.pop(0)
					A2 = []
					for i in range(4):
						A2.append([int(j) for j in contents.pop(0).split(' ')])
					pr = Problem(a1,A1,a2,A2)
					print pr.toString()
					res = pr.solve()
					fout.write('Case #'+str(count)+': '+str(res)+'\n')
					count += 1

			fout.close()
		except NameError as e:
			print e
		except AttributeError as e:
			print e
		except IOError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

class Problem:
	def __init__(self,a1,A1,a2,A2):
		self.a1 = int(a1)
		self.a2 = int(a2)
		self.A1 = A1
		self.A2 = A2

	def solve(self):
		try:
			sol1 = self.A1[self.a1-1]
			sol2 = self.A2[self.a2-1]
			common = []
			for i in sol1:
				if i in sol2:
					common.append(i)
			print sol1, sol2, common
			if len(common)==1:
				return common[0]
			elif len(common)==0:
				return 'Volunteer cheated!'
			else:
				return 'Bad magician!'
		except NameError as e:
			print e
		except TypeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

	def toString(self):
		print 'a1: '+str(self.a1)+'\n'+'A1: '+str(self.A1)+ '\n' + 'a2: '+str(self.a2)+ '\n' + 'A2: '+str(self.A2)


if __name__ == '__main__':
	#ir = InputReader('sample.in')
	ir = InputReader('/Users/david/Downloads/A-small-attempt0.in')