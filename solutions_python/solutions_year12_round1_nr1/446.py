#!/usr/bin/python
import sys

def getwp(pros, n):
	p =1
	for i in range(0, n):
		p = p * pros[i]	

	return p
def case1(c, t, pros):
	i=0
	tp = 1
	for pro in pros:
		tp = tp * pro
		
	res = (t - c + 1)* tp + ( t - c + 1 + t + 1) * ( 1 - tp)

	return res

def case2(c, t, pros):
	res=[]
	tp = 1

	nt = t - c + 3
	
	for i in range( 1, c+1 ):
		#press i back;
		p = getwp(pros, c-i)
		t1 = ( i + ( t - ( c - i ) ) + 1 )
		tres = t1 * p + (t1+t+1)*(1-p)

		res.append(tres)

	return res

def case3(c, t, pros):
	# press enter
	return 1 + t + 1 

def treatcase(case):
	line1 = case[0]
	line2 = case[1]
	
	tarr = line1.split()
	current = int(tarr[0])
	total = int(tarr[1])
	#print "Current: %d, total:%d "%(current, total)
	
	tarr = line2.split()
	pros = []
	for te in tarr:
		pros.append(float(te))

	if len(pros) != current:
		print "Error............"
		return -1

	res = case2(current, total, pros)
	#print res
	res.append(case1(current, total, pros))
	res.append(case3(current, total, pros))

	ret = res[0]
	#print res
	for tr in res:
		#print "Comparing %f and %f "%(ret, tr)
		if ret >= tr:
			ret = tr

	return ret
	
def testmain():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	#print "Cases:" , Ts
	lines = []
	while True:
		line=f.readline()
		#print "read line ", line
		if(len(line)<=0):
			break
		lines.append(line.strip())

	#print lines	
	cases = []
	i=0
	while i < len(lines):
		case = lines[i:i+2]
		cases.append(case)
		i += 2

	#print cases
	j=0
	for case in cases:
		j += 1
		res = treatcase(case)
		print "Case #%d: %.6f"%(j, res)
	
if __name__ == "__main__":
	testmain()
