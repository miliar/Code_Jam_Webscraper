

def process(line):
	s_max, s = line.split()
	s_max = int(s_max)
	s = [int(char) for char in s]
	total_friends = 0
	total_standing = 0
	
	
	for index in range(s_max + 1):
		if total_standing >= index:
			total_standing += s[index]
		else:
			total_friends += 1
			total_standing += 1 + s[index]
		if s_max < total_standing:
			break
		
	#print(total_friends)
	return total_friends
	

def main():
#	input = '''4
#4 11111
#1 09
#5 110011
#0 1'''
	with open("A-large.in", "r") as input:
		with open("output.txt", "w") as output:		
			first_line = True
			case = 1
			
			for line in input:
				#print(line)
				if first_line:
					first_line = False
					continue
				else:
					friends = process(line)
					
					output.write("Case #" + str(case) + ": " + str(friends) + "\n")
					case += 1


	#print(a)
	
	
main()
#process("6 0000001")
#process("6 4009704")
#process("3 0001")
#process("4 20011")
#process("4 90001")
#process("6 2300501")
