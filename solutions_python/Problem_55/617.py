input = open("C-small.in","r")
output = open("C-small.out","w")
tests = int(input.readline())

for i in range(0,tests):
	line_raw = input.readline()
	line = line_raw.rsplit(' ')
	rounds =  int(line[0])
	seats = int(line[1])
	num = int(line[2])
	
	line_raw = input.readline()
	sizes = line_raw.rsplit(' ')
	itr = 0
	curr = 0 #number of people
	total = 0 #total number of people
	starts = {0:0} #itr:number of people until itr
	indexes = {0:0}
	for r in range(0,rounds):
		curr=0
		for j in range(0,seats):
			curr = curr + int(sizes[(itr+j)%num])
			if curr>seats or ((itr+j)%num == itr and j!=0):
				curr = curr - int(sizes[(itr+j)%num])
				itr = (itr + j)%num
				break
				

		total=total+curr
		#if itr in starts:
		#	total = total +(total-starts[itr])*(int(float((rounds-r))/((r-indexes[itr])))) 
		#	break
		#starts[itr]=total
		#indexes[itr]=r
	output.write("Case #"),i+1,":",total
	output.write(str(i+1))
	output.write(": ")
	output.write(str(total))
	output.write("\n")
	