def read():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	result=[]
	for i in range(1, t + 1):
		nb = list(str(input()))
		l = len(nb)
		for j in range(l):
			nb[j]=int(nb[j])

		totest = l-1
		while totest!=0:
			test = ok(nb,totest)
			if test is False:
				print(nb)
				change(nb,totest)
				print(nb)
				totest = l-1
			else:
				totest -=1
		total = 0
		for i in range(l):
			total+=nb[l-i-1]*(10**i)
		result.append(total)

	f1=open('tidy.out', 'w+')
	for i in range(1, t + 1):
		f1.write("Case #{}: {}\n".format(i,result[i-1]))
		print("Case #{}: {}".format(i,result[i-1]))

def change(nb,i):
	for j in range(i,len(nb)):
		nb[j]=9
	nb[i-1]-=1

def ok(nb,i):
	for j in range(i):
		if nb[j]>nb[i]:
			return False
	return True

if __name__ == '__main__':
	read()

