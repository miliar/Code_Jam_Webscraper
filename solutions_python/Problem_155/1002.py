import sys

def calculate(strN):
	voy=int(strN[0])
	ret=0
	for i in xrange(1, len(strN)):
		if voy>=i:
			voy+=int(strN[i])
		else:
			agrego=(i-voy)
			ret+=agrego
			voy+=agrego+int(strN[i])
	return ret
		

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
    	file.readline()
    	case=1
    	for line in file.readlines():
    		if not line.strip(): continue
    		result = calculate(line.strip().split(" ")[1])
    		print "Case #"+str(case)+": "+str(result)
    		case+=1