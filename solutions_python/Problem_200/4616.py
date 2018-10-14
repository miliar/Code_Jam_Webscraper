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
	fi=open("TidyNumbersAnswer.txt","w")
	for i in range(int(input[0])):
		temp=0
		arr=input[i+1].strip("\n")
		if(len(arr)==1):
			answer=arr
		else:
			urut=True
			temp2=1
			for j in range(len(arr)-1):
				if(arr[j]>arr[j+1]):
					urut=False
					break
			if(urut):
				answer=arr
			else:
				for j in range(len(arr)-1):
					if(arr[j]>=arr[j+1]):
						temp=j
						break
			
				arr=list(arr)
				arr[temp]=str(int(arr[temp])-1)
				for j in range(j+1,len(arr)):
					arr[j]=str(9)
				if (arr[0]==str(0)):
					arr.remove(arr[0])
				arr=''.join(arr)
				answer=arr
		fi.write("Case #")
		fi.write(str(i+1))
		fi.write(": ")
		fi.write(answer)
		if(i!=int(input[0])-1):
			fi.write("\n")
	fi.close()	
		
	
if __name__ == "__main__":
	main()
