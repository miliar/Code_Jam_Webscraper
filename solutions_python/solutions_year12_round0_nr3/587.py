def compute(a, b):
	cnt = 0;
	digCnt = len(str(a));
	newB = str(b)
	tMap = {}
	for v in range(a, b):
		num = str(v)
		tMap.clear()
		for i in range(0,digCnt):
			newNum = num[-i:]+num[0:-i]
			pairNum = newNum.lstrip('0')
			if pairNum != newNum:
				continue;
			if pairNum<=num or pairNum>newB :
				continue;
			tMap[pairNum]=1
		cnt = cnt + len(tMap);
	return cnt

def myTest():
	a = 1000000
	b= 2000000
	for i in range(1):
		print compute(187,950);


def test():
	f = open("C-large.in")
	lines = f.readlines()
	i=1;
	for line in lines[1:]:
		line = line.strip('\n');
		contents = line.split(' ');
		cnt = compute(int(contents[0]), int(contents[1]));
		print "Case #"+str(i)+":", cnt
		i = i + 1

#myTest()
test()
