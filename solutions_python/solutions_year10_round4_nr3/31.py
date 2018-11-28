import math

MAX_SIZE = 105

def help(array):
	exit = -2
	count = 0
	while(exit != 0):
		count += 1
		temp = range(0,MAX_SIZE)
		for k in range(0,MAX_SIZE):	
			temp[k] = range(0,MAX_SIZE)
			for j in range(0,MAX_SIZE):
				temp[k][j] = 0
			
		
		temp[0][0] = 0
		for a in range(1,MAX_SIZE):
			if (array[0][a-1] == 1):
				temp[0][a] = array[0][a]
			else:
				temp[0][a] = 0
			
			if (array[a-1][0] == 1):
				temp[a][0] = array[a][0]
			else:
				temp[a][0] = 0		

		
		for a in range(1,MAX_SIZE):	
			for b in range(1,MAX_SIZE):
				if (array[a][b-1] == array[a-1][b]):
					temp[a][b] = array[a][b-1]
				else:
					temp[a][b] = array[a][b]
					
		for a in range(0,MAX_SIZE):	
			for b in range(0,MAX_SIZE):
				if (temp[a][b] == 1):
					exit = -1
				array[a][b] = temp[a][b]
				
		if (exit == -1):
			exit = -2
		else:
			exit = 0
		
	return count

def getResult(array):
	for a in range(0,MAX_SIZE):	
		for b in range(0,MAX_SIZE):
			if array[a][b] == 1:
				return help(array)
	return 0
	
	


	
if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	array = range(0,MAX_SIZE)
	for k in range(0,MAX_SIZE):
		array[k] = range(0,MAX_SIZE)

	for i in range(1,num+1):
		r = int(f.readline().strip())
		for k in range(0,MAX_SIZE):
			for x in range(0,MAX_SIZE):
				array[k][x] =0

		for j in range(0,r):
			(x1,y1,x2,y2) = map(int,f.readline().strip().split(" "))
			for a in range(x1,x2+1):
				for b in range(y1,y2+1):
					array[a][b] = 1
		ans = 0
		ans = getResult(array)
		print "Case #%d: %s" %(i,ans)