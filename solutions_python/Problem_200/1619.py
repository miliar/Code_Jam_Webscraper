def string_to_list (s):
	length = len (s)
	number_list = []
	for i in s:
		number_list.append(int(i))
	return (number_list)

def test (s):
	number = string_to_list(s)
	length = len(s)
	out =""
	for x in range(length-1):
		number_front = number[x]
		number_back  = number[x+1]
		if number_front > number_back:

			for front in range(x):

				if number [x-front] != number [x-front-1]: 
					number[x-front] = number[x-front]-1
					for z in range (x-front+1, length):
						number[z] = 9
					break

				if x - front -1 == 0:
					number[x - front -1 ] = number[x - front -1 ] -1
					for z in range(x-front,length):
						number[z]= 9
					break
					
			if x == 0:
				number[x] = number[x]-1
				for z in range (x+1,length):
					number[z]= 9

			break
		
	if number[0] ==0 and length > 1:
		del number[0]

	for e in number:
		out = out + str(e) 
	return(out)



case_num = 1
input_path = "../Downloads/B-large.in"
out = open('answer.txt', 'w')
with open(input_path) as f:
    lines = f.readlines()
    lines_head = lines[0]
    lines_body = lines[1:]
    for element in lines_body:
	    input_element =  element.rstrip() # remoce \n
	    #input_element_array = input_element.split()
	    #time_number = str(test(input_element_array[0], int(input_element_array[1])))
	    number = test(input_element)
	    answer = "Case #"+ str(case_num) +": "+ number
	    print(answer)
	    out.write(answer+'\n')
	    case_num = case_num +1

out.close()