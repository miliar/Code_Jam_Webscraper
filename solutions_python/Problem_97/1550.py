arq = open('numbersresult.txt' , 'w')
t , i , c = int(raw_input()) , 1 , 0

while t != 0 :
	line = str(raw_input()).split()
	a , b = int(line[0]) , int(line[1])
	r = range(int(a) , int(b) + 1)	
	l = []

	for n in r :
		N , k = str(n) , 1

		while k != len(N) :
			M = N[k:] + N[0:k]
			
			if int(N) < int(M) and (int(M) < b or int(M) == b) :
					temp = [int(N) , int(M)]
					
					if temp not in l :
						l.append(temp)

			k = k + 1

	arq.write('Case #%d: ' %(t - (t - i)) + '%d' %len(l) +'\n')

	t , i = t - 1 , i + 1
