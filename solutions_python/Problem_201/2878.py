#!\Python34\python
from __future__ import print_function
import os
import timeit

def main():
	fo=open("input.IN")
	input=[]
	for i in fo:
		input.append(i)
	fo.close()
	fi=open("BathroomStallAnswer.txt","w")
	for i in range(1,int(input[0])+1):
		a,b=input[i].split(' ')
		a,b=int(a),int(b)
		arr=[a]
		if(b>1):
			for j in range(b-1):
				temp=max(arr)
				arr.remove(temp)
				if(temp%2==1):
					arr.append(temp//2)
					arr.append(temp//2)
				else:
					arr.append((temp//2)-1)
					arr.append(temp//2)
		temp=max(arr)
		if(temp%2==1):
			ans1=str(temp//2)
			ans2=str(temp//2)
		else:
			ans1=str(temp//2)
			ans2=str((temp//2)-1)
		fi.write("Case #")
		fi.write(str(i))
		fi.write(": ")
		fi.write(ans1)
		fi.write(' ')
		fi.write(ans2)
		fi.write("\n")
	fi.close()	
		
	
if __name__ == "__main__":
	main()
