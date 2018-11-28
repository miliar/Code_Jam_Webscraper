import sys
def main():
	fin=open(sys.argv[1],'r')
	fout=open(sys.argv[2],'w')
	nums=eval(fin.readline())
	for i in range(nums):
		temp=fin.readline()
		temp=temp.split()
		test(int(temp[0]),int(temp[1]),i+1,fout)
		print int(temp[0]),int(temp[1]),i+1
	fin.close()
	fout.close()

def test(start,end,case,fout):
	if end<10:
		fout.write("Case #"+str(case)+": 0\n")
	else:
		count = 0
		lst=[]
		while(start<=end):
			print start," ",
			temp_str=str(start)
			i=0
			length=len(temp_str)
			while(i<length):
				tempval=int(temp_str[i:length]+temp_str[0:i])
				if(tempval>start) and (tempval<=end) and (find(lst,start,tempval)<1):
					count +=1
					lst.append((start,tempval))
				print tempval, " ",
				i+=1
			print 
			start+=1
		
		fout.write("Case #"+str(case)+": "+str(count)+"\n")

def find(lst,val1,val2):
	for item in lst:
		if (item[0]==val1 and item[1]==val2) or (item[0]==val2 and item[1]==val1):
			print val1,val2
			return 1
	else:
		return 0


if __name__=='__main__':
	main()
