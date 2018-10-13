import numpy as np
import time
start_time = time.time()

def palindrome_array(array):
	array=np.array(array).astype(int)
	rev=np.zeros(array.size).astype(int)
	while (array > 0).any():
		mod=np.ones(array.size).astype(int); mod[np.where(array>0)]=10
		dig = array % mod
		rev = rev * mod + dig
		array = array / mod
	return rev

f = open('C-small-attempt1.in','r')
input_data=f.readlines()[::-1]
f.close()
output = open('C-output.txt','w')

T=int(input_data.pop().rstrip())

for case in range(T):
	output.write('Case #'+str(case+1)+': ')
	lookup_range=np.array(map(int, input_data.pop().rstrip().split()))
	lookup_table=np.array(range(np.ceil(np.sqrt(lookup_range[0])).astype(int),1+np.floor(np.sqrt(lookup_range[1])).astype(int)))
	lookup_table=lookup_table[np.where(palindrome_array(lookup_table)==lookup_table)]
	squares=lookup_table*lookup_table
	find = np.count_nonzero(palindrome_array(squares)==squares)
	output.write(str(find)+"\n")
	print("Progress : " +str(case+1)+" / "+str(T)+"\033[F")

elapsed_time = time.time() - start_time
print "\nElapsed Time: "+str(elapsed_time)+"\nAverage Elapsed Time per case: "+str(elapsed_time/T)+"\n"