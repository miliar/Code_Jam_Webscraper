import sys
maxWithSurprise = {28:10,27:10,26:10,25:9,24:9,23:9,22:8,21:8,20:8,19:7,18:7,17:7,16:6,15:6,14:6,13:5,12:5,11:5,10:4,9:4,8:4,7:3,6:3,5:3,4:2,3:2,2:2}
maxNormal = {30:10,29:10,28:10,27:9,26:9,25:9,24:8,23:8,22:8,21:7,20:7,19:7,18:6,17:6,16:6,15:5,14:5,13:5,12:4,11:4,10:4,9:3,8:3,7:3,6:2,5:2,4:2,3:1,2:1,1:1,0:0}

def processline(line):
	input = map(int,line.split())
	n = input[0]
	s = input[1]
	p = input[2]
	result = 0
	testcases = sorted(input[3:3+n])
	for score in testcases:
		if s>0:
			if score in maxWithSurprise:
				if maxWithSurprise[score] >= p:
					result += 1
					s -= 1
			else:
				if maxNormal[score] >= p:
					result += 1
		else:
			if maxNormal[score] >= p:
				result += 1			
	return str(result)





def main():
    from sys import stdin, stdout
    first_in = stdin.readline()
    testcasecount = int(first_in)
    inputs = stdin.readlines()
    count = 1
    for indx in range(testcasecount):
        line = inputs[indx]
        print "Case #"+str(count)+": "+processline(line)
        count += 1

if __name__ == "__main__":
    main()