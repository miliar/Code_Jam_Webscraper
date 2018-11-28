def main():
	file_in=open("input1.in",'r')
	file_out=open("output.txt",'w')
	
	cases=file_in.readline()
	
	for i in range(int(cases)):
		limit=file_in.readline().strip('\n').split()
		
		result=calc(limit)
		final='Case #'+str(int(i)+1)+': '+str(result)+'\n'
		file_out.write(final)


def calc(limit):
	a=int(limit[0])
	b=int(limit[1])
	num=''	
	case=0
	li=list()
	li_i=list()
	for i in range(a,b+1):
		num=str(i)
		l=len(num)-1
		for j in range(l,0,-1):
			num=str(i)
			dummy=num[j:]
			num=num[:j]
			num=str(dummy)+str(num)
			if (int(num)<=b and int(num)>i and int(num)>=a):
				flag=0
				for p,q in zip(li,li_i):
					if ((int(num)==p and i==q) or (i==p and int(num)==q)):
						flag=1
						break
				if flag!=1:
					case=case+1
					li.append(int(num))
					li_i.append(i)
	
	return case
	
main()

