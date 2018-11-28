from sys import stdin
from sys import argv
script,file = argv
def input():
	f = open("{}.in".format(file))
	lines = f.readlines()
	T = int(lines[0])
	for i in range(1,T+1):
		line1 = lines[i].split()
		#print(line1)
		line2 = line1[1]
		#print(line2)
		A1 = [int(j) for j in line2]
		A2 = int(line1[0])
		output(A1,A2,i)
		A1 = []
def output(array,s_max,test):
	count = 0
	sum1 = 0
	#print(s_max)
	#print(array)
	for i in range(1,s_max+1):
		sum1 = sum1 + array[i-1]
		#print(sum1)
		if sum1 < i:
			count = count + 1
			sum1 = sum1 + 1
	with open("{}.out".format(file),'a') as f:
		f.writelines("Case #{}: {}\n".format(test,count))

if __name__ == "__main__":
	input()
