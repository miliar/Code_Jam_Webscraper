def test (s,k):
	length = len(s)
	time = 0
	for i in range(length-k+1) :
		if s[i] == '-':
			for x in range(k):
				if s[i+x] == "-" :
					s = s[:i +x] + '+' + s[x+i+1:] 
				elif s[i+x] == "+" :
					s = s[:i +x] + '-' + s[x+i+1:] 
			time = time + 1
			
	for z in range (k):
		if s[-z]=='-':
			time = "IMPOSSIBLE"

	return time

#test('---+-++-',3)
case_num = 1
input_path = "../Downloads/A-large.in"
out = open('answer.txt', 'w')
with open(input_path) as f:
    lines = f.readlines()
    lines_head = lines[0]
    lines_body = lines[1:]
    for element in lines_body:
	    input_element =  element.rstrip()
	    input_element_array = input_element.split()
	    time_number = str(test(input_element_array[0], int(input_element_array[1])))
	    answer = "Case #"+ str(case_num) +": "+time_number
	    print(answer)
	    out.write(answer+'\n')
	    case_num = case_num +1

out.close()