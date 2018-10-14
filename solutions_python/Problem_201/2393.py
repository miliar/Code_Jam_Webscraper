def frkn(n,k):
	n = int(n); k = int(k); A = [n]; i = 1
	while k > i:
		x = (A[0]-1)/2
		A += [A[0]-1-x, x]
		del A[0]
		A = sorted(A)[::-1]
		i += 1
	x = (A[0]-1)/2
	return "{} {}".format(A[0]-1-x, x)



inp = open("/root/Desktop/input.txt","r")
output = open("/root/Desktop/output.txt","w")

inp_ = inp.read().splitlines()

i = 1

for x in inp_:
	x = x.split(" ")
	
	out = "Case #{}: {}\n".format(i,frkn(x[0],x[1]))
	output.write(out)
	i += 1

inp.close()	
output.close()









