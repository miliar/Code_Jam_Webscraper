def judge(data,a):
    n = int(data[0])
    pd = int(data[1])
    pg = int(data[2])
    if pg == 0 and pd != 0:
	return False
    if pd == 100:
	return True
    if pg == 100 and pd != 100:
	return False
    if n >= 100:
	return True
    for i in range(1,n + 1):
	t = i * pd / 100.0
	if int(t) == t:
	    return True
    return False

def gcd(x,y):
    if x % y == 0:
	return y
    return gcd(y,x % y)

def main():
    filein = open('testin.txt','r')
    fileout = open('textout.txt','w')
    text = filein.readline()
    n = 2000
    a = []
    a.append(0)
    for i in range(1,100):
	a.append(int(100 / gcd(i,100)))
    for i in range(1,n + 1):
	textline = filein.readline()
	isPossible = judge(textline.split(),a)
	if isPossible == True:
	    fileout.write('Case #%d: Possible\n' % (i))
	else:
	    fileout.write('Case #%d: Broken\n' % (i))
    filein.close()

main()

