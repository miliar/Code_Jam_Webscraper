import sys
import string    

def main():
	f=open(sys.argv[1],'r')
    	num=f.readline()
    	num=int (num)
    	result=0
	i=0
	while (num!=0):
		i=i+1
		r=f.readline()
		t=int(r.split(' ',1)[1])
		r=int(r.split(' ',1)[0])
		while (t!=0):
			area=((r+1)*(r+1)-(r*r))
			if (t>=area):
				result=result+1
				t-=area
			else:
				break
			r=r+2
		print 'Case #'+str(i)+': '+str(result)
		result=0
		num=num-1
if __name__== '__main__':
    main()
