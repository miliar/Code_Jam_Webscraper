def gcd(a,b):
	while b!= 0:
		t = b
		b = a %b
		a = t
	return a



if __name__ == "__main__":

	fobj = open("fairwarning_output.txt","w")
	T = int(raw_input())
	for each_testcase in range(1,T+1):

		input = raw_input().split(' ')
		N = int(input[0])
		input.pop(0)

		T = sorted(list(set([ long(i) for i in input ])))
		input=[]
		diff_list =[]
		for i in range(0,len(T)-1):
			diff_list.append(T[i+1]-T[i])

		print diff_list
		GCD=0
		if len(diff_list)== 1:
			GCD=min(diff_list)
		else:
			for i in range(0,len(diff_list)-1):
				if i==0:
					GCD = gcd(diff_list[i+1],diff_list[i])
				else:
					GCD = gcd(diff_list[i+1],GCD)

		first = min(T)
		print GCD
		if GCD <= 1:
			y=0
		else:
			i=1
			while(True):
				y = (GCD*i) - first
				if y >=0:
					break
				i=i+1

		fobj.write( "Case #"+str(each_testcase)+": "+str(y)+"\n" )
	fobj.close()