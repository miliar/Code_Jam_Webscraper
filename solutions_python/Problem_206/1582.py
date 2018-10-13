#import matplotlib.pyplot as plt

def horsewalk(distance, horseSpeeds):
	
	#lines = list(map(lambda h: ((h[0], 0), (distance, (distance-h[0]) / h[1])), horseSpeeds))
	
	#for line in lines:
	#	plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]])
	
	hs = list(map(lambda h: (distance-h[0]) / h[1], horseSpeeds))
	maxh = max(hs)

	#plt.plot(distance, maxh, '^')
	#plt.show()
	
	return distance / maxh
	
count = int(input())
for i in range(count):
	line = input()
	
	distance = int(line.split()[0])
	
	def readHorse():
		line = input()
		return int(line.split()[0]), int(line.split()[1])

	horseSpeeds = [readHorse() for i in range(int(line.split()[1]))]
	print("Case #"+str(i+1)+":", horsewalk(distance, horseSpeeds))
