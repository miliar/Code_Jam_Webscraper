
def check_asc(max):
	i = 1
	temp = max[0]
	while (i < len(max)):
		if (temp > max[i]):
			return False
		temp = max[i]
		i = i +1
	return True

def a():
    Test = input(); # for Tests
    count = 0 # for counting
    list = []
    while (Test != 0):
    	Test = Test - 1
    	count = count - 1
    	check = 1 
    	max = raw_input()
    	while (check == 1): # till you find that number
    	 	if(check_asc(max)):
    	 		list = list + [max]
    	 		break
    	 	max = str(int(max) - 1)
    for i in range(0, len(list)):
    	print "Case #%d: %s"%(i + 1, list[i])

    		

a()




			
			
			
	
		
	