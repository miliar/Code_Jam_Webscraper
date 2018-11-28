inputfile = 'B-large.in'
outputfile = 'outputfile.txt'

fi = open(inputfile)
fo = open(outputfile, 'w')

test_cases = int(fi.readline())
for case in range(test_cases):
	line = fi.readline()
	line = line.split(' ')
	C = float(line[0])
	F = float(line[1])
	X = float(line[2])
 
	time = 0.0
	no_of_cookies = 0
	cookies_per_second = 2.0	
	
	while(True):	
		time_required_to_buy = float(C/cookies_per_second)
		time_before_buy = float(X/cookies_per_second)
		cookies_per_second_after_buy = F + cookies_per_second
           	time_after_buy = float(X/cookies_per_second_after_buy + time_required_to_buy)

            	if time_before_buy < time_after_buy:
                	time = float(time + time_before_buy)
               		no_of_cookies = no_of_cookies + cookies_per_second * time;
            	else:
                	time = float(time + time_required_to_buy)	
	                no_of_cookies = no_of_cookies + cookies_per_second * time_required_to_buy
        	        cookies_per_second = F + cookies_per_second

        	if no_of_cookies >= X:
                	fo.write('Case #' + str(case+1)+ ': %.7f\n'%time)
                	break	
			
fi.close()
fo.close()	

