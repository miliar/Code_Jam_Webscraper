def result(a,b,k):
	number = 0
	for i in range(a):
		for j in range(b):
			if(a<=k or b<=k):
				number+=1
			else:
				binand = int(dec_to_bin(i),2) & int(dec_to_bin(j),2)
				if(binand<k):
					number+=1

	return number

def dec_to_bin(x):
    return (str)(bin(x)[2:])
	
T = int(raw_input())
for t in range(T):
	s = raw_input()
	x = [int(elem) for elem in s.split()]	
	A = x[0]
	B = x[1]
	K = x[2]
	print "Case #" + str(t+1) + ":", result(A,B,K)


		
