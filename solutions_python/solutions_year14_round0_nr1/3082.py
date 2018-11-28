# Function
def read_my_file(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        output = open("A-small-attempt2.out", "w")
        for t in range(T):
	        R1 = None
	        R2 = None
	        A1 = int(f.readline())
	        for i in range(4):
	        	if i == (A1 - 1):
	        		R1 = (f.readline()).split()
	        	else:
	        		f.readline()
	        A2 = int(f.readline())
	        for i in range(4):
	        	if i == (A2 - 1):
	        		R2 = (f.readline()).split()
	        	else:
	        		f.readline()
	        answers = {x: 1 for x in R1}
	        count = 0
	        number = None
	        for x in R2:
	        	if x in answers:
	        		number = x
	        		count+=1
	        output.write("Case #%d: " % (t+1))
	        if count > 1:
	        	output.write("Bad magician!\n")
	        else:
		        if count == 0:
	        		output.write("Volunteer cheated!\n")
	        	# print "Case #3: Volunteer cheated!"
	        	if count == 1:
	        		output.write(number + "\n")
# Python note:
if __name__ == '__main__':
    read_my_file('A-small-attempt2.in')