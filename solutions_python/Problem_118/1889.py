import math
def cpal(s):
	length = len(s)
	for j in xrange(0,length/2):
    		if s[j] != s[(length-1)-j]: 
		        return False
	return True
T = raw_input()
for k in range(int(T)):
	count = 0
	inp = raw_input()
	inp = inp.split(' ')
	start  = int(math.ceil(math.sqrt(int(inp[0]))))
	end = int(math.floor(math.sqrt(int(inp[1]))))
	for i in xrange(start,end+1): 
		 if(cpal(str(i)) and cpal(str(i*i))):
			count = count+1
	print("Case #"+str(k+1)+": "+str(count)) 

