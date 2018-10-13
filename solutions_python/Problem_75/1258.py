#to run this type python magicka.py > B-small-attempt0.out

f = open('B-small-attempt0.in', 'r')
cases_number = int(f.readline())

def treat(case,number):
	elements=case.split()
	combine_number=int(elements[0])
	combines=elements[1:combine_number+1]
	opposed_number=int(elements[combine_number+1])
	opposed=elements[combine_number+2:combine_number+2+opposed_number]
	number_invoked=elements[-2]
	invoked=elements[-1]
	result=""
	for letter in invoked:
		found = False
		for i in range(combine_number):
			if letter in combines[i]:
				combine1=letter
				combine2=combines[i][(combines[i].index(letter)+1)%2]
				combine3=combines[i][2]
				if len(result)!=0:
					if result[-1] == combine2:
						found = True
						result=result[:len(result)-1]+combine3
				break
		if found == False:
			for j in range(opposed_number):
				if  letter in opposed[j]:
					opposed2=opposed[j][(opposed[j].index(letter)+1)%2]
					if opposed2 in result:
						found = True
						result=""
		if found == False:
			result=result+letter
		result1=""
		for let in result:
			result1=result1+let+", "
	print "Case #"+str(number+1)+": ["+result1[:-2]+"]"
	
for number in range(cases_number):
	case=f.readline()
	treat(case,number)
