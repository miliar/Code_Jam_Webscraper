#!/usr/bin/python
lookup=['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']
def translate(a):
	c=""
	for i in a:
		if ord(i)==32:
			c=c+" "
		else:
			c=c+lookup[ord(i)-97]
	return c
def main():
	a=raw_input()
	a=int(a)
	count=1
	while a>0:
		a=a-1
		b=raw_input()
		print "Case #"+str(count)+":",translate(b)
		count=count+1
if __name__=="__main__":
	main()	
