import math

n=[]
k=[]
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  stalls, persons = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  n.append(stalls)
  k.append(persons)



def func(stalls):
	half= (stalls//2)
	f_half = stalls -1 - half

	return f_half,half


# sections=[]
# persons= 1
# stalls = 1000

max_ans = []
min_ans = []

for ni, ki in zip(n,k): 
	persons = ki
	stalls =ni
	sections=[]

	while persons>0:
		small, big = func(stalls)
		

		
		sections.append(small)
		sections.append(big)

		
		stalls = max(sections)

		if stalls in sections:
			sections.remove(stalls)	


		persons-=1	

	# print (max((small,big)))
	# print (min((small,big)))
	max_ans.append(max((small,big)))
	min_ans.append(min((small,big)))

# print(max_ans)
# print(min_ans)

#print(n)
for i in range(1,t+1):
	print("Case #{}: {} {}".format(i, max_ans[i-1] , min_ans[i-1]))
