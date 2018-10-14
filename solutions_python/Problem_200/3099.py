num= int(input())



for i in range (num):

	line=input()
	prev='0'

	for ind, val in enumerate(line):
		#print( str(ind) +val)
		if val < prev:	#see if the previous one is bigger. this is the frist one that 
						#is in the wrong order.

			#print("prev: {} curr_ind: {}".format(prev, ind))
			curr_ind=ind #the one we're looking at rn
			line=line[:curr_ind-1]+ str( int(line[curr_ind-1]) -1) + '9'* (len(line[curr_ind:]))
			#print("after first change, line: {}".format(line))
			curr_ind-=1
			#print("after first change, curr_ind:{}".format(curr_ind))
			
			while curr_ind > 0:
				prev= line[curr_ind-1]
			#	print("inside loop, prev:{}".format(line[curr_ind-1]))

				if prev <= line[curr_ind]:
					break
				else:
					line=line[:curr_ind-1]+ str( int(line[curr_ind-1]) -1) + '9'* len(line[curr_ind:])
					curr_ind-=1
			break	
		else:
			prev=val

	line= str(int(line))




	print("Case #{}: {}".format(i+1, line))