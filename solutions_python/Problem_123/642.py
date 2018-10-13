#! /bin/python

class Game:

	def __init__(self, file):
		tmp=file.readline()
		a, b = tmp.split()
		self.life,self.nb_motes=int(a),int(b)

		tmp=file.readline().split()
		self.motes=[]
		for i in xrange(self.nb_motes):
			self.motes.append(int(tmp[i]))

		self.motes.sort()


	def resolve(self):
		i, nb_actions=0,0
		while i<self.nb_motes:
			
			#print "on mange du : " + str(self.motes[i])+" avec du "+str(self.life)

			if self.life>self.motes[i]:
				self.life+=self.motes[i]



			else:
				nb_actions_sup=0
				while self.life<=self.motes[i] and nb_actions_sup<(self.nb_motes-i):
					self.life+=(self.life-1)
					nb_actions_sup+=1
					#print str(self.life)

				if nb_actions_sup>=(self.nb_motes-i):
					return nb_actions+nb_actions_sup
				else:
					nb_actions+=nb_actions_sup
					self.life+=self.motes[i]

			i+=1
			#print ">>"

		return nb_actions


#data=open("A-small-attempt0.in", "r")
data=open("data", "r")
nb_games=int(data.readline())

for i in xrange(nb_games):

	g=Game(data)
	print "Case #"+str(i+1)+": "+str(g.resolve())