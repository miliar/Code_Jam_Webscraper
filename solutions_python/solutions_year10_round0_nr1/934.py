#Snapper Chain

class Snapper:
	def __init__(self, count, parent=None):
		self.child = None
		self.parent = parent
		self.power = 0
		self.state = 0
		self.light = "OFF"
		if count > 1:
			count -= 1
			self.child = Snapper(count,self)
	def snap(self):									
		
		if self.power == 1:
			if self.state == 0: self.state = 1
			else: self.state = 0
		
		if self.parent != None:
			if self.parent.power == 1 and self.parent.state == 1:
				self.power = 1				
			else: self.power = 0						

		if self.child != None:
			self.child.snap()
		else:
			if self.power == 1 and self.state == 1:
				self.light = "ON"
			else: self.light = "OFF"
			
	def lite(self):
		temp = self
		while temp.child != None:
			temp = temp.child
		return temp.light
		
f = open("A-small-attempt3.in","r")
w = open("snap_out.txt","w")
N = int(f.readline())
for i in range(1, N+1):
	S = map(int, f.readline().split())
	snap = Snapper(S[0])
	snap.power = 1
	for j in range(0,S[1]):
		snap.snap()
	w.write("Case #{0}: {1}\n".format(i, snap.lite()))
	del snap
f.close()
w.close()