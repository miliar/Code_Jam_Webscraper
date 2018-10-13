def main():
	tt = int(input())
	for i in range(1,tt+1):
		a = input()
		t = a.split(" ")
		m = int(t[0])
		n = int(t[1])
		while n>1:
			if n%2==1:
				if m%2==0:
					m = int(m/2)
					m -= 1
				else:
					m = int(m/2)
			else:
				m = int(m/2)
			n = int(n/2)
		if m%2==1:
			print ("Case #{}: {} {}".format(i,int(m/2),int(m/2)))
		else:
			print ("Case #{}: {} {}".format(i,int(m/2),int(m/2)-1))

if __name__ == '__main__':
	main()