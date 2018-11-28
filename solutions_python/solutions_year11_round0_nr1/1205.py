import sys

class Robot:
	def __init__(self,color,todo):
		self.color = color
		self.todo = todo

		#must know: where i am, where i'm going, when i press
		self.loc = 1
		self.nextLoc = 0
		self.nextPress = 0

		#print todo
		self.findNext(0)

	
	def done(self):
		if self.nextLoc == 0:
			return True
		return False

	def findNext(self,press):

		gotten = False

		#print "Finding next press for %s - turn is %d"%(self.color,press)

		for i in range(press*2 , len(self.todo) , 2):
			#print " - i=%d : c = %s, todo[%d]=%s"%(i,self.color,i,self.todo[i])
			if self.todo[i] == self.color:
				self.nextLoc = int(self.todo[i+1])
				self.nextPress = i/2
				gotten = True
				break

		if not gotten:
			#no next.  we're done
			self.nextLoc = 0


	def go(self,press):
		if self.nextLoc == 0:
			#I'm done
			return 0

		if self.loc == self.nextLoc:
			#we're where we need to be

			if press < self.nextPress:
				#waiting
				return 0
			else:
				#PUSH!!
				self.findNext(press+1)
				return 1
		else:
			#move
			if self.loc < self.nextLoc: self.loc += 1
			else: self.loc -= 1
			return 0

	
	def show(self):
		print "%s: I'm at %d, and need to be at %d for press %d"%(self.color,self.loc,self.nextLoc,self.nextPress)


def main(fileN):

	#fileN = raw_input("File: ")
	f = open(fileN,"r")
	lines = f.read().split("\n")

	T = int(lines[0])

	for t in range(T):
		test = t+1
		line = lines[test]
		lineA = line.split()

		buttons = int(lineA[0])
		todo = lineA[1:]

		O = Robot("O",todo)
		B = Robot("B",todo)


		turns = 0
		presses = 0
		while not (B.done() and O.done() ):

			#print "Turn %d (%d presses):"%(turns,presses)
			#O.show()
			#B.show()

			pressed = 0
			pressed += O.go(presses)
			pressed += B.go(presses)

			if pressed > 1: print "ALERT!!"

			presses += pressed

			turns+=1

			#raw_input()

		print "Case #%d: %d"%(test,turns)


if __name__ == '__main__':
	main(sys.argv[1])
