import sys
import random

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
					N = contents.pop(0)
					NB = [float(j) for j in contents.pop(0).split(' ')]
					KB = [float(j) for j in contents.pop(0).split(' ')]
					pr = Problem(N,NB,KB)
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
	def __init__(self,N,NB,KB):
		self.N = int(N)
		self.NB = NB
		self.KB = KB

	def solve(self):
		try:
			score1 = self.playDWar(self.N,self.NB,self.KB)
			score2 = self.playWar(self.N,self.NB,self.KB)
			print score1,score2
			return str(score1)+' '+str(score2)
		except ValueError as e:
			print e
		except TypeError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

	def playWar(self,N,NB,KB):
		nb = NB[:]
		kb = KB[:]
		war_score = 0
		for i in range(N):
			Chosen_N = min(nb)
			Chosen_K = kb[0]
			for j in sorted(kb, reverse = True):
				if j > Chosen_N:
					Chosen_K = j
			if Chosen_N > Chosen_K:
				#print Chosen_N, Chosen_K
				war_score += 1
			nb.remove(Chosen_N)
			kb.remove(Chosen_K)
		return war_score

	def playDWar(self,N,NB,KB):
		nb = NB[:]
		kb = KB[:]
		war_score = 0
		for i in range(N):
			Chosen_N = min(nb)
			Told_N = max(nb)
			Chosen_K = kb[0]
			for j in sorted(kb, reverse = True):
				if j > Told_N:
					Chosen_K = j
			print Chosen_N, Told_N, Chosen_K
			if Told_N > Chosen_K:
				#print 'ups'+ ' '+ str(Chosen_N)
				for j in sorted(nb, reverse = True):
					if j > Chosen_K:
						Chosen_N = j
				#print 'ups'+ ' '+ str(Chosen_N)

			print Chosen_N, Told_N, Chosen_K
			print '-'
			if Chosen_N > Chosen_K:
				war_score += 1
			nb.remove(Chosen_N)
			kb.remove(Chosen_K)
		return war_score

	def toString(self):
		print 'N: '+str(self.N)+'\n'+'NB: '+str(self.NB)+ '\n' + 'KB: '+str(self.KB)


if __name__ == '__main__':
	#ir = InputReader('sample.in')
	ir = InputReader('/Users/david/Downloads/D-large.in')