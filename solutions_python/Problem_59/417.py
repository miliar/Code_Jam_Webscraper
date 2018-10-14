class Node:
	def __init__(self):
		self.exists = False
		self.name=''
		self.c={}#key:exists?
	
	def create(self,content):
		if self.c.get(content) == None:
			t = Node()
			t.name=content
			self.c[content]=t
			#print "creating:"+self.c[content].name
			return self.c[content]
		else:
			return self.c[content]
	def toggle(self,content):
		if self.c.get(content) != None:
			t = self.c[content]
			t.exists = True
			return t
		else:
			return None
			

def doIt(current,root):
	v=root
	
	for i in current:
		v=v.create(i)
def toggleIt(current,root):
	v=root
	for i in current:
		v=v.toggle(i)
		if v == None:
			return
	
	
def checkIt(n):
	k=0
	for nn in n.c.values():
		#print "Name:"+nn.name
		if nn.exists==False:
			k=k+1
		k=k+checkIt(nn)
	return k

N= eval(raw_input())		
for i in range(0,N):
	root=Node()
	#print root.c.values()
	root.exists=True
	l=raw_input().split()
	E = eval(l[0])
	NE = eval(l[1])
	

	L=[]
	for j in range(0,E):
		L.append(raw_input())
	for j in range(0,NE):
		current = raw_input().split('/')
		current.remove('')
		doIt(current,root)
	for j in L:
		exists = j.split('/')
		exists.remove('')
		toggleIt(exists,root)
	print "Case #"+str(i+1)+": "+str(checkIt(root))