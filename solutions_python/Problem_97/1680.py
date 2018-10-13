import sys 


if len(sys.argv) > 1 and sys.argv[1]: 
	f = open(sys.argv[1])
	a = f.read()
	f.close()
else:
	a = '''4
	1 9
	10 40
	100 500
	1111 2222'''

c = a.split('\n')

def check(s):
	e = s.split(' ')
	cnt = 0
	cntStr = '|'
	for i in range(int(e[0]), int(e[1])):

		string = str(i)
		firstStr = string[0] 
		isOkay = False 

		for k in string:
			if k != firstStr:
				isOkay = True
				break
			else:
				isOkay = False
			firstStr = k
			
		if i > 9 and isOkay:
			for j in range(1,len(string)):
				if int(e[1]) >= int(string[j:] + string[:j]) > i >= int(e[0]) and cntStr.find('|' + string + ',' + string[j:] + string[:j] + '|') == -1:
					cntStr += string + ',' + string[j:] + string[:j] + '|'
					#cntStr += string[j:] + string[:j] + '|'
					cnt += 1
		else:
			cnt = cnt
	return cnt 

if len(sys.argv) > 2 and sys.argv[2]:
	w = file(sys.argv[2], 'w')
else:
	w = file('C-small-0.out', 'w')

for i in range(int(c[0])):
	
	#result = check(c[i+1])
	w.write('Case #%d: %d\n' % (i+1, check(c[i+1])))
	#print 'Case #%d: %d\n' % (i+1, check(c[i+1]))

w.close()

