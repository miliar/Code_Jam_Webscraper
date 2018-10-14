def getOutput(i,a1,a2,m1,m2):
	filename = "output";

	array1 = m1[int(a1)-1]
	array2 = m2[int(a2)-1]
	ans = set(array1).intersection(set(array2))
	
	if len(ans) == 1:
		answer = ans.pop()
	elif len(ans) > 1:
		answer = "Bad magician!"
	elif len(ans) == 0:
		answer = "Volunteer cheated!"

	f = open(filename,'a')
	f.write("Case #"+str(i)+": "+str(answer) + "\n")

def main():
	with open('A-small-attempt0.in', 'r') as f:
  		first_line = f.readline()

	  	for i in range(int(first_line)):
	  		mat1 = []
  			mat2 = []	
	  		
	  		answer1 = f.readline()
	  		
	  		for j in range(4):
	  			mat1.append(f.readline().split())
	  		answer2 = f.readline()
	  		
	  		for j in range(4):
	  			mat2.append(f.readline().split())
	  		getOutput(i+1,answer1,answer2,mat1,mat2)
	  		
if __name__ == "__main__":
	main()