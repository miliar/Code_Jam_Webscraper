class Robot:
	def __init__(self, objectifs):
		self.Obj=objectifs
		self.pos=1
		if len(self.Obj)>0: (self.NB,self.NC)=self.Obj.pop(0)
		else: (self.NB,self.NC)=(-1,-1)

	def move(self, count):
		if self.NC==-1: 
			#print("rien a faire")
			return (0, count)
		if self.pos < self.NB : 
			self.pos += 1
			#print("avance vers", self.NB) 
			return (1,count)
		if self.pos > self.NB:
			self.pos -=1
			#print("retourne vers", self.NB)
			return (1,count)
		#print("je suis a", self.NB)
		if self.NC==count :
			#print("appuie sur", self.NB)
			count += 1
			if len(self.Obj)>0: 
				(self.NB,self.NC)=self.Obj.pop(0)
				#print("nouvel objectif:",self.NB)
			else: 
				self.NC=-1
				#print("plus d'objectif:")
		return (1,count)
	
T=int(input())
for t in range(1, T+1):
	args=[x for x in input().split()]
	N=int(args.pop(0))
	OObj=list()
	BObj=list()
	for n in range(N):
		color=args.pop(0)
		if color=='O':
			OObj.append((int(args.pop(0)),n))
		else:
			BObj.append((int(args.pop(0)),n))
	#print("O:",OObj)
	#print("B:",BObj)
	time=0
	count=0
	O=Robot(OObj)
	B=Robot(BObj)
	#print(O.Obj)
	work=2
	while work > 0 :
		(wo,count1)=O.move(count)
		(wb,count2)=B.move(count)
		count=max(count1,count2)
		work=wo+wb
		time+=1
		#print("time:",time,"work:",work)
		#toto=input()
		
	print("Case #"+str(t)+":",time-1)