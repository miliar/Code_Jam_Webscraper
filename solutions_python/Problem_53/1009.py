file=open("input","w")

class Power:
	def __init__(self):
		pass
	def get_power(self):
		return True
class Snaper:
	def __init__(self,prev):
		self.on=False
		self.has_power=False
		self.prev=prev
	def reset(self):
		self.on=False
		self.has_power=False
		return self
	def clap(self):
		if self.has_power:
			self.on = not self.on
	def clap2(self):
		self.has_power=self.prev.get_power()
	def get_power(self):
		return self.has_power and self.on

snapers_pool=[]
power=Power()
snapers_pool.append(Snaper(power))
for i in range(30):
	snapers_pool.append(Snaper(snapers_pool[i]))
T=int(raw_input())

for i in range(T):
	N,K=map(int,raw_input().split(' '))
	snapers=map(lambda x : x.reset(),snapers_pool[:N])
	snapers[0].clap2()
	for k in range(K):
		map(lambda x : x.clap(),snapers)
		map(lambda x : x.clap2(),snapers)
	if snapers[N-1].get_power():
		result="ON"
	else:
		result="OFF"
	file.write("Case #"+str(i+1)+": "+result+"\n")
