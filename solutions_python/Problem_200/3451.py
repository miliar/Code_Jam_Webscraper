def istidy(n):
	for i in range(len(n)-1):
		if n[i+1] < n[i]:
			return False
	return True


def bigtidy(n):

	while not istidy(n):
		for i in range(len(n)-1):
			if n[i+1] < n[i]:
				n = n[:i]+str(int(n[i])-1)+"9"*(len(n)-i-1)
				break
	return int(n)
		

inp = open("/root/Desktop/input.txt","r")
output = open("/root/Desktop/output.txt","w")

inp_ = inp.read().splitlines()

i = 1

for x in inp_:
	out = "Case #{}: {}\n".format(i,bigtidy(x))
	output.write(out)
	i += 1

inp.close()	
output.close()









