

a = open('A-large.in','r') 
	# data = a.read().split('\n')
b = open('b.txt','w') 

def magic(Des,N,Km,Speed):
# Des = 100
# N = 2
# Km = [80,70]
# Speed = [100,10]
	Time = []

	for i in range(N):
		Time.append((float(Des-Km[i]))/Speed[i])

	# print Time
	annie_time = max(Time)
	if annie_time == 0:
		return 0
	return (float(Des)/annie_time) 


T = int(a.readline())
for i in range(T):
	Des, N = map(int,a.readline().split(' '))
	Km = []
	Speed = []
	for j in range(N):
		km , spd = map(int,a.readline().split(' '))
		Km.append(km)
		Speed.append(spd)
	b.write ('Case #%s: '%(i+1)+str(magic(Des,N,Km,Speed))+'\n')
	# print 'Case #%s: '%(i+1)+str(magic(Des,N,Km,Speed))+'\n'