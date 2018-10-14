

file_in = open("B-small-attempt0.in","r")
file_out = open("output.txt","w")

T = int(file_in.readline())
k = 0

while(k<T):
	A,B,K = file_in.readline().split(' ')
	A = int(A)
	B = int(B)
	K = int(K)

	num_ways = 0

	cat_tickets = range(0, K)
	mach_A = range(0, A)
	mach_B = range(0, B)

	for val_A in mach_A:
		for val_B in mach_B:
			if (cat_tickets.count(val_A&val_B)) > 0:
				num_ways+=1

	file_out.write("Case #" + str(k+1) + ": " + str(num_ways))
	file_out.write("\n")

	k+=1

file_in.close()
file_out.close()