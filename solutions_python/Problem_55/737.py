
fread=open('C:\Users\Sandip\Desktop\C-small-attempt0.in','r')
#fread=open('C:\Users\Sandip\Desktop\A-large.in','r')
#fread=open('C:\Users\Sandip\Desktop\.in','r')
fwrite=open('C:\Users\Sandip\Desktop\C.out','w')


total_cases=fread.readline().strip()
for i in range(int(total_cases)):
	#print "NEW CASE\n"
	line1 = fread.readline().strip()
	l1= line1.split()
	R = int(l1[0]) # R =number of rounds
	k= int (l1[1]) # k = max seat
	n= int(l1[2]) # n = number of groups
	line2 = fread.readline().strip()
	groups_size_list= line2.split()
	
	
	total_size = 0
	for j in range(n):
		groups_size_list[j] = int(groups_size_list[j])
		total_size = total_size + groups_size_list[j]
		
	if total_size <= k: # all can be seated together.
		total_money_made = total_size * R
		o_string="Case #"+str(i+1)+": "+str(total_money_made)+"\n"
		fwrite.write(o_string)
		continue
	
	total_money_made = 0
	ptr = 0
	for r in range(R):
		size=0
		while size + groups_size_list[ptr] <=k :
			size = size + groups_size_list[ptr]
			if ptr == n-1:
				ptr = 0
			else:
				ptr = ptr + 1
		
		total_money_made = total_money_made + size
		
	o_string="Case #"+str(i+1)+": "+str(total_money_made)+"\n"
	fwrite.write(o_string)
		
	

fread.close()
fwrite.close()


