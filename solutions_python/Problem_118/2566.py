import math
f = open('3_small.in','r')
lines = f.readlines()
f.close()

n = int(lines[0])
output = ''
for i in range(n):
	interval = lines[i+1].split()
	num_sum = 0;
	
	for j in range(int(interval[0]),int(interval[1])+1):
		reverse_j = int(str(j)[::-1])
		
		if reverse_j == j:		
			
			sqrt_j = math.sqrt(j)
			
			if math.floor(sqrt_j) == sqrt_j:
				sqrt_j = int(sqrt_j)
				reverse_sqrt = int(str(sqrt_j)[::-1])
				
				if reverse_sqrt == sqrt_j:
					num_sum+=1
	
	output+= 'Case #' + str(i+1) + ': ' + str(num_sum)+'\n'
			
f = open('3.out','w')
f.write(output)
f.close()
