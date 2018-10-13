def solve(number) :
	if len(number) > 2 :
		for i in range(len(number) - 2,0,-1) : 
			if int(number[i]) < int(number[i - 1]) : 
				number[i - 1] = str(int(number[i - 1]) - 1)
				for j in range(i, len(number) - 1) :
					number[j] = '9'

f = open('test.in', 'r')
l = f.readlines()
size = l[0]
for i in range(1,int(size) + 1):
	l_aux = list(l[i])
	solve(l_aux)
	print ('Case #' + str(i) + ': ' + str(int(''.join(l_aux))))

