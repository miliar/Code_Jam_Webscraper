fileot=open("a.txt",'w')
def main():

	with open('B-large.in', 'r') as f:
		a=f.readlines()
	N=int(a[0])
	for i in range(0,N):
		calc(a[1+i],1+i)


def calc(stri,d):
	no=stri.split(' ')
	for i in range(0,len(no)):
		no[i]=float(no[i])
	C=no[0]
	F=no[1] 
	X=no[2]
	t=0.00000
	f=2.00000
	try:
		while(1):
			if (C/f)+(X/(F+f))>X/f:
				t=t+X/f
				raise StopIteration
			else:
				t=t+(C/f)				
				f=f+F
	except StopIteration:
		{}
		
	fileot.write("Case #"+str(d)+": "+str(t)+"\n")
if __name__ == "__main__":
    main()
