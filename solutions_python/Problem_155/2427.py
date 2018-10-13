read_file=open("input.txt","r")
write_file=open("output.txt","w")
i=int(read_file.readline())
for j in range(i):
	total,array=read_file.readline().split()
	total=int(total)
	s=0
	current=0
	difference=0
        fc=0
	for index in range(total+1):
		current=int(array[index])
		if s<index:
			diff=index-s
			fc=fc+diff
			s=s+diff
			
		s=s+current
			
	write_file.write("Case #")
	write_file.write(str(j+1))
	write_file.write(": ")
	write_file.write(str(fc))
	write_file.write('\n')



