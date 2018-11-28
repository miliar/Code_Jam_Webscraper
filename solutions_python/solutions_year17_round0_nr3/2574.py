def read():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	result=[]
	for i in range(1, t + 1):
		result.append((0,0))
		bath_length ,people = [int(s) for s in input().split(" ")]
		bathroom = []
		for j in range(bath_length):
			bathroom.append(0)
		for j in range(people):
			result[i-1] = chose(bathroom)
	f1=open('bathroom.out', 'w+')
	for i in range(1, t + 1):
		f1.write("Case #{}: {} {}\n".format(i,result[i-1][0],result[i-1][1]))


def chose(bathroom):
	stall = 0
	scoremax = -1
	maxifinal = -1
	for i in range(len(bathroom)):
		if bathroom[i]==0:
			r = computer(bathroom,i)
			l = computel(bathroom,i)
			if l>=r:
				score = r
				mini =r
				maxi = l
			if r>l:
				score=l
				mini = l
				maxi = r

			if score>=scoremax:
				if maxi>maxifinal or score> scoremax:
					stall = i
					scoremax=score
					minifinal = mini
					maxifinal = maxi
	bathroom[stall]=1
	return(maxifinal,minifinal)


def computel(bathroom,i):
	l = i
	while l>-1 and bathroom[l]==0:
		l-=1
	return i-l-1

def computer(bathroom,i):
	l = i
	while l<len(bathroom) and bathroom[l]==0:
		l+=1
	return l-i-1


if __name__ == '__main__':
	read()

