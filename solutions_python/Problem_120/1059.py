def main():
	inpu=open("A-small-attempt0.in",'r')
	output=open("sample.out","w+")
	total=int(inpu.readline())

	for i in range(total):
		temp=inpu.readline().split(" ")
		r=int(temp[0])
		paint=int(temp[1])
		n=1
		cost=2*r+4*n-3
		print cost
		if cost>paint:
			n=0
		else:
			while cost<=paint:
				n+=1
				print cost,n, str(2*r+4*n-3)
				cost=cost+2*r+4*n-3

				print cost, n, paint
			n-=1
		output.write("Case #%d: %d\n"%(i+1, n))

main()