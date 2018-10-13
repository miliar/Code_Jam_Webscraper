def convert(a,b):
	add = a%b
	if a<=1:
		return str(a)
	else:
		return str(convert(a//b,b)) + str(add)
a=int(input())
for i in range(a):
	b=int(input())
	convert(b,10)

	while(b):
		c=str(b)
		for j in range(len(c)-1):
			if c[j:j+1]>c[j+1:j+2]:
				b-=1
				break		

		if c==str(b):
			print("Case #"+str(i+1)+": "+c)
			break