t = input()

for ctr_does_not_matter_here in range(1,t+1):

	n = input()
	n = str(n)

	while 1==1:
		new_no = ""
		prev_bit='0'
		flag=0

		for bit in n:
			if(int(bit) < int(prev_bit)):
				l = len(new_no)
				no_to_be_changed = int(new_no[l - 1])

				if(l>1): 
					new_no = new_no[0:l-1]
				else:
					new_no = ""
				new_no += str(no_to_be_changed - 1)

				for j in range(l,len(n)):
					new_no += '9'
				flag=1
				break
			else:
				new_no += bit
			prev_bit = bit

		if(flag==0): break
		n = str(int(new_no))

	print "Case #" + str(ctr_does_not_matter_here) + ": " + new_no


