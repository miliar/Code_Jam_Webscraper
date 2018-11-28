f = open("tidyNumbersSmall.in", "r")
new_file = open("tidyNumbersSmallSol", "w")
t = int(f.readline())

# def last_counted_number (n):
# 	splitted_number = str(n)
# 	if len(splitted_number) == 1:
# 		return splitted_number
	
# 	last_counted_number = []

# 	for i in range(0,len(splitted_number) - 1):
# 		current = splitted_number[i]
# 		next = splitted_number[i+1]
# 		if current <= next:
# 			last_counted_number.append(current)
# 		else:
# 			if current == '1':
# 				return '9'*(len(splitted_number) - 1)
# 			else: 
# 				last_counted_number.append(str(int(current)-1))
# 				for j in range(i,len(splitted_number)-1):
# 					last_counted_number.append('9')
# 			return ''.join(last_counted_number)
# 	last_counted_number.append(splitted_number[-1])
# 	return ''.join(last_counted_number)

def brute_force_tidy(n):
	if check_if_steady(n):
		return n
	for i in range(0,n):
		if check_if_steady(n - i):
			return n-i

def check_if_steady(k):
	number_list = list(str(k))
	for i in range(0, len(number_list) - 1):
		if number_list[i+1] < number_list[i]:
			return False
	return True
for i in range(1,t+1):
	n = int(f.readline())
	new_file.write("Case #"+str(i)+ ": "+str(brute_force_tidy(n))+"\n")