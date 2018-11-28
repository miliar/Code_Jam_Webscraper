from math import sqrt

def palindrome(num):
	num_str=str(num)
	if '.' in num_str:
		a=num_str.find('.')
		num_str1=num_str[:a]
		return num_str1 == num_str1[::-1]	
	return num_str == num_str[::-1]
	

def perf_square(num):
	sq_r = sqrt(num)
	newsq_r = str(sq_r)
	a=newsq_r.find('.')
	return((len(newsq_r[a+1:]) == 1) and (newsq_r[-1]=='0'))
       



def sq_palin(a,b):
	counter=0
	for i in range(a,b+1):
		if palindrome(i) and perf_square(i) and palindrome(i** 0.5):
			counter = counter+1
			
	return counter
with open('/home/cybercam/Desktop/C-small-attempt3.in') as f:
    num_tc=f.readline().strip()
    fo=open('/home/cybercam/Desktop/C-small-attempt0.txt', 'wb')
    for j in range(int(num_tc)):
	    testcases=f.readline().strip().split()
	    print testcases
	    fo.write('Case #'+str(j+1)+':'+' '+str(sq_palin(int(testcases[0]),int(testcases[1])))+'\n')
fo.close()


