import pdb

def get_ascending(number):
	number = int(number)
	previous_val = -1
	is_ascending = False
	ascending = False
	while not is_ascending:
		list_of_ints = map(int,str(number))
		for i in list_of_ints:
			#pdb.set_trace()
			if previous_val <= i:
				is_ascending = True
			else:
				is_ascending = False
				number = number -1
				previous_val = -1
				break;
			previous_val = i
	print number
	return number

def main():
	i = 1
	with open('google.txt', 'rb') as fp:
		next(fp)
		for line in fp:
			if line:
	#			pdb.set_trace()
				answer = get_ascending(line.rstrip())
				with open('answers.txt', 'a') as a:
					answer = str(answer)
					i = str(i)
					a.write("Case #"+i+": "+answer+"\n")
					i = int(i)
				i = i + 1
if __name__ == '__main__':
	main()	
