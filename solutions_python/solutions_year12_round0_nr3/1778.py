#!/usr/bin/python
def codejam(a,b):
	list=[]
	count=0
	for i in range(a,(b+1)):
		c=str(i)
		d=len(c)
		list.append(i)
		for j in range(1,d):
			str1=c[:j]
			str2=c[j:]
			str1=str2+str1
			h=int(str1)
			if h>=a and h<=b and (h!=i) and (h not in list):
				count=count+1
	return count

def main():
	a=raw_input()

	a=int(a)
	count=1
	while a>0:
		a=a-1
		b=raw_input()
		b=b.split()	
		c=int(b[0])
		d=int(b[1])
		e=codejam(c,d)
		print "Case #"+str(count)+":",e
		count=count+1
if __name__=="__main__":
	main()	
