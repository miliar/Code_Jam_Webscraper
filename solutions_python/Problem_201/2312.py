import math
file=open("C-small-2-attempt0.in",'r')
t=int(file.readline())
out=open("out5.txt",'w')

def numb(n,k):
	h=int(math.log(k)/math.log(2))
	partition=2**(h)
	place=int(partition/2)
	k=k-partition+1
	if n%2 == 0:

			even = n
			even_c = 1
			odd = -1
			odd_c = 0

	else:

		even = -1
		even_c = 0
		odd = n
		odd_c = 1

	for j in range(h):

		temp_evenc = 0
		temp_oddc = 0
		temp_even = -1
		temp_odd = -1

			
		if even_c > 0:

			if (int(even/2))%2 == 0:

				temp_even = int(even/2)
				temp_odd = int(even/2)  - 1


			else:

				temp_even = int(even/2)  - 1
				temp_odd = int(even/2)

			temp_evenc += even_c
			temp_oddc += even_c


		if odd_c > 0: 

			if (int(odd/2)) %2 == 0: 

				temp_even = int(odd/2)
				temp_evenc += 2*odd_c

			else:

				temp_odd = int(odd/2)
				temp_oddc += 2*odd_c


		even = temp_even
		odd = temp_odd
		even_c = temp_evenc
		odd_c = temp_oddc

	if even > odd:

		large = even
		large_c = even_c
		small = odd
		small_c = odd_c


	else:

		large = odd
		large_c = odd_c
		small = even
		small_c = even_c

	

	if k <= large_c:

		return large


	else:

		return small

		


for i in range(1,t+1):
	[n,k]=file.readline().split()
	[n,k]=[int(n),int(k)]
	temp=numb(n,k)
	if temp%2==0:
		out.write('Case #%d: %d %d\n'%(i,int(temp/2),(int((temp/2)-1))))	
	else:
		out.write('Case #%d: %d %d\n'%(i,int(temp/2),int(temp/2)))
			
	
