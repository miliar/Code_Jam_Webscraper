def getAnswer(i,array):
	
	filename = "output";

	c = float(array [0])
	f = float(array[1])
	x = float(array[2])

	threshold = x/2
	time = 0
	startRate = 2
	time = 0

	while(1):
		newtime = time + (c/startRate) + (x/(startRate+f))
		if(newtime < threshold):
			time = time + (c/startRate)
			threshold = newtime
			startRate = startRate + f
		else:
			#print round(threshold,7)
			break
	
	f = open(filename,'a')
	f.write("Case #"+str(i)+": "+str(threshold) + "\n")

def main():
	with open('B-large.in', 'r') as f:
  		first_line = f.readline()

	  	for i in range(int(first_line)):
	  		getAnswer(i+1,f.readline().split())

if __name__ == "__main__":
	main()