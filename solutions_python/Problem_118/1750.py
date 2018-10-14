from math import ceil

f = open('C-small-attempt0.in')

numbers_input = f.readline().split(' ')
T = int(numbers_input[0])

j = 1
for line_input in f:
	count = 0
	I_min, I_max = (int(i)**0.5 for i in line_input.split(' '))
	I_max = int(I_max)
	I_min = ceil(I_min)
	min_len = len(str(I_min))
	max_len = len(str(I_max))
	
	if min_len == 1:
		if I_min <= 1:
			count += 3
		elif I_min <= 2:
			count += 2
		elif I_min <= 3:
			count += 1
	
	elif min_len % 2 == 1:
		start_bin = 1 << (min_len // 2 - 1)
		finish_bin = 1 << (min_len // 2)
		while start_bin < finish_bin:
			if I_min <= int(bin(start_bin)[2:]+'0'+bin(start_bin)[2:][::-1]):
				count += (finish_bin - start_bin)*3 + 2
				break
			elif I_min <= int(bin(start_bin)[2:]+'1'+bin(start_bin)[2:][::-1]):
				count += (finish_bin - start_bin)*3 + 1
				break
			elif I_min <= int(bin(start_bin)[2:]+'2'+bin(start_bin)[2:][::-1]):
				count += (finish_bin - start_bin)*3
				break
			start_bin += 1
		else:
			if I_min <= int(str(2*10**(min_len // 2 - 1))+'0'+str(2*10**(min_len // 2 - 1))[::-1]):
				count += 2
			elif I_min <= int(str(2*10**(min_len // 2 - 1))+'1'+str(2*10**(min_len // 2 - 1))[::-1]):
				count += 1
				
	elif min_len % 2 == 0:
		start_bin = 1 << (min_len // 2 - 1)
		finish_bin = 1 << (min_len // 2)
		while start_bin < finish_bin:
			if I_min <= int(bin(start_bin)[2:] + bin(start_bin)[2:][::-1]):
				count += (finish_bin - start_bin) + 1
				break
			start_bin += 1
		else:
			if I_min <= int(str(2*10**(min_len // 2 - 1)) + str(2*10**(min_len // 2 - 1))[::-1]):
				count += 1
	
	if max_len == min_len:
	
		if max_len == 1:
			if I_max >= 3:
				pass
			elif I_max >= 2:
				count -= 1
			elif I_max >= 1:
				count -= 2
		
		elif max_len % 2 == 1:
			if I_max >= int(str(2*10**(max_len // 2 - 1))+'1'+str(2*10**(max_len // 2 - 1))[::-1]):
				pass
			elif I_max >= int(str(2*10**(max_len // 2 - 1))+'0'+str(2*10**(max_len // 2 - 1))[::-1]):
				count -= 1
			else:
				start_bin = (1 << (max_len // 2)) - 1
				finish_bin = (1 << (max_len // 2 - 1)) - 1
				while start_bin > finish_bin:
					if I_max >= int(bin(start_bin)[2:]+'2'+bin(start_bin)[2:][::-1]):
						count -= (2**(max_len//2 - 1)*3 + 2) - (start_bin - finish_bin)*3
						break
					elif I_max >= int(bin(start_bin)[2:]+'1'+bin(start_bin)[2:][::-1]):
						count -= (2**(max_len//2 - 1)*3 + 2) - (start_bin - finish_bin)*3 + 1
						break
					elif I_max >= int(bin(start_bin)[2:]+'0'+bin(start_bin)[2:][::-1]):
						count -= (2**(max_len//2 - 1)*3 + 2) - (start_bin - finish_bin)*3 + 2
						break
					start_bin -= 1
					
		elif max_len % 2 == 0:
			if I_max >= int(str(2*10**(max_len // 2 - 1))+str(2*10**(max_len // 2 - 1))[::-1]):
				pass
			else:
				start_bin = (1 << (max_len // 2)) - 1
				finish_bin = (1 << (max_len // 2 - 1)) - 1
				while start_bin > finish_bin:
					if I_max >= int(bin(start_bin)[2:]+bin(start_bin)[2:][::-1]):
						count -= (2**(max_len//2 - 1) + 1) - (start_bin - finish_bin)
						break
					start_bin -= 1
		
	
	
	
	elif max_len == 1:
		if I_max >= 3:
			count += 3
		elif I_max >= 2:
			count += 2
		elif I_max >= 1:
			count += 1
	
	elif max_len % 2 == 1:
		if I_max >= int(str(2*10**(max_len // 2 - 1))+'1'+str(2*10**(max_len // 2 - 1))[::-1]):
			count += (2**(max_len // 2 - 1)) * 3 + 2
		elif I_max >= int(str(2*10**(max_len // 2 - 1))+'0'+str(2*10**(max_len // 2 - 1))[::-1]):
			count += (2**(max_len // 2 - 1)) * 3 + 1
		else:
			start_bin = (1 << (max_len // 2)) - 1
			finish_bin = (1 << (max_len // 2 - 1)) - 1
			while start_bin > finish_bin:
				if I_max >= int(bin(start_bin)[2:]+'2'+bin(start_bin)[2:][::-1]):
					count += (start_bin - finish_bin)*3
					break
				elif I_max >= int(bin(start_bin)[2:]+'1'+bin(start_bin)[2:][::-1]):
					count += (start_bin - finish_bin)*3 - 1
					break
				elif I_max >= int(bin(start_bin)[2:]+'0'+bin(start_bin)[2:][::-1]):
					count += (start_bin - finish_bin)*3 - 2
					break
				start_bin -= 1
			
	elif max_len % 2 == 0:
		if I_max >= int(str(2*10**(max_len // 2 - 1))+str(2*10**(max_len // 2 - 1))[::-1]):
			count += (2**(max_len // 2 - 1)) + 1
		else:
			start_bin = (1 << (max_len // 2)) - 1
			finish_bin = (1 << (max_len // 2 - 1)) - 1
			while start_bin > finish_bin:
				if I_max >= int(bin(start_bin)[2:]+bin(start_bin)[2:][::-1]):
					count += (start_bin - finish_bin)
					break
				start_bin -= 1
	
	for i in range(min_len+1, max_len):
		if i%2 == 1:
			count += 2**(i//2 - 1)*3 + 2
		else:
			count += 2**(i//2 - 1) + 1
	
	print('Case #%d: %d' % (j, count))
	j += 1