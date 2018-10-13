import os
import sys

def main():
	input = sys.argv[1]
	output = sys.argv[2]
	with open(input) as i:
		with open(output,'w') as o:
			number = int(i.readline())
			for j in range(number):
				l = i.readline()
				l = l.strip()
				l = l.split()
				c,f,x = map(float,l)
				o.write("Case #")
				o.write(str(j+1))
				o.write(": ")
				o.write(str(round(cookie(c,f,x,2),7)))
				o.write('\n')


def howlong(h,x):
	return x/h
	

def cookie(c,f,x,p):
	t = 0
	notbuy = howlong(p,x)
	buy = howlong(p,c) + howlong(p+f,x)

	while notbuy > buy:
		t = t + howlong(p,c)
		p = p+f
		notbuy = howlong(p,x)
		buy = howlong(p,c) + howlong(p+f,x)

	return t + notbuy


if __name__ == "__main__":
	main()
