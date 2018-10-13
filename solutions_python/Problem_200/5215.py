#
# Tidy Numbers
#


import sys
x = sys.stdin.readlines()

for i in range(0,len(x)):

	x[i] = int(x[i].rstrip())


#list of inputs
for j in range(1,len(x)):
	
	tidy_nums = [0]

	#range
	for i in xrange(1,x[j]+1):
		i = str(i)

		#all single digits OK
   		if len(str(i)) == 1:
       			tidy_nums.append(int(i))

		elif len(str(i)) > 1:
			# solve for numbers made of repeat ints
			if i.count(i[0]) == len(i):
            			tidy_nums.append(int(i))
			
			#solve for all other numbers
    			elif all(i[k] <= i[k+1] for k in range(len(i)-1)):	
				tidy_nums.append(int(i))
        		

    		else:
        		continue

	print 'Case #'+str(int(j))+':', tidy_nums[-1]
	           
            
        
        

