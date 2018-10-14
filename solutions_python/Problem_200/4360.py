def tidy(number):
	"""
	input : string of number
	output :  last tidy number counted. 
	"""
	result=[]
	for item in number:
		result.append(int(item))


	for item in range(len(result)-1):
		if result[item]>result[item+1]:
			index_change=item
			if index_change!=0:
				while result[index_change]==result[index_change-1]:
					index_change-=1
			result[index_change]-=1
			for change_to_9 in range(index_change+1,len(result)):
				result[change_to_9]=9

	output=''
	if result[0]==0:
		result=result[1:]

	for item in result:
		output+=str(item)
	return output

# print tidy('132')
# print tidy('1000')
# print tidy('7')
# print tidy('111111111111111110')



f_out = open('B_output_small1.txt', 'w')
f_in = open('B-small-attempt1.in', 'r')

lines = [line.strip() for line in f_in.readlines()][1:]

#lines=['132','1000','7','111111111111111110']
# for item in range(len(lines)):
# 	print 'Case#',item+1, lines[item]
print lines

for idx in range(len(lines)):
	
	ans = tidy(lines[idx]) 
	
	# writes an answer (in a new line) to the output file
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()




#print tidy('303')


