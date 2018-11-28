import sys
import re

class InputReader:
	def __init__(self,filePath):
		try:
			f = open(filePath)
			contents = f.readlines()
			f.close()
			T = contents.pop(0)
			with open('output.out','w') as fout:
				count = 1
				while len(contents) > 0:
					print '***************'
					print len(contents)
					line = contents.pop(0)
					smax = line.split(' ')[0]
					audience = line.split(' ')[1]
					pr = Problem(smax,audience)
					print pr.toString()
					res = pr.solve()
					fout.write('Case #'+str(count)+': '+str(res)+'\n')
					count += 1

			fout.close()
		except TypeError as e:
			print e
		except IOError as e:
			print e
		except NameError as e:
			print e
		except AttributeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

class Problem:
	def __init__(self,smax,audience):
		self.smax = smax
		self.audience = audience
		self.mapa = {}

	def solve(self):
		try:

			#Building hash map
			counter = 0
			#print self.audience
			for person in self.audience:
				if(person != '\n'):
					#print person + '->' + str(counter)
					self.mapa[counter] = int(person)
					counter = counter + 1

			# Count the persons needed
			
			need = 0
			k = 0
			energy = 0

			i = 1
			while i < int(self.smax) + 1:
				k = k + self.mapa[i-1]
				if ( k < i ):
					need = need + 1
					k = k + 1
				i = i + 1
			#print k, need
			return need
		except TypeError as e:
			print e
		except NameError as e:
			print e
		except AttributeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

	def toString(self):
		print 'SMax: '+str(self.smax)+' --> Audience: '+str(self.audience)


if __name__ == '__main__':
	#ir = InputReader('sample.in')
	ir = InputReader('/Users/david/Downloads/A-large.in')