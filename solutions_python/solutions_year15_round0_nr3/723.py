import sys

def calculate(fullLine):
	res="1"
	tengoI=""
	tengoJ=""
	tengoK=""
	alternativeList=[]
	for c in xrange(len(fullLine)):
		res=tabla[res][fullLine[c]]
		alternativeList.append(res)
	if "i" in alternativeList and "k" in alternativeList:
		if alternativeList.index("i")<(len(alternativeList)-1-alternativeList[::-1].index("k")) and alternativeList[-1]=="-1":
			return "YES"
		else:
			return "NO"
	else:
		return "NO"
		

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
    	file.readline()
    	case=1
    	tabla={}
    	tabla["1"]={"i":"i", "j": "j", "k":"k"}
    	tabla["-1"]={"i":"-i", "j": "-j", "k":"-k"}
    	tabla["i"]={"i":"-1", "j": "k", "k":"-j"}
    	tabla["-i"]={"i":"1", "j": "-k", "k":"j"}
    	tabla["j"]={"i":"-k", "j": "-1", "k":"i"}
    	tabla["-j"]={"i":"k", "j": "1", "k":"-i"}
    	tabla["k"]={"i":"j", "j": "-i", "k":"-1"}
    	tabla["-k"]={"i":"-j", "j": "i", "k":"1"}
		
    	for line in file.readlines():
    		if not line.strip(): continue
    		if len(line.split(" "))==2:
    			repite=int(line.split(" ")[1])
    		else:
    			result = calculate(line.strip()*repite)
    			print "Case #"+str(case)+": "+result
    			case+=1