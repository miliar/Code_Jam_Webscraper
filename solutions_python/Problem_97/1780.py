'''
Created on 14-Apr-2012

@author: RAJAT
'''
def main():
	file_a=open("C-small-attempt1.in",'r')
	file_b=open("output.txt",'w')
	
	cases=file_a.readline()
	
	for i in range(int(cases)):
		case=file_a.readline().strip('\n').split()
		
		result=calc(case)
		final='Case #'+str(int(i)+1)+': '+str(result)+'\n'
		file_b.write(final)


def calc(case):
	a=int(case[0])
	b=int(case[1])
	num=''	
	case=0
	list_a=list()
	list_b=list()
	for i in range(a,b+1):
		num=str(i)
		l=len(num)-1
		for j in range(l,0,-1):
			num=str(i)
			temp=num[j:]
			num=num[:j]
			num=str(temp)+str(num)
			if (int(num)<=b and int(num)>i and int(num)>=a):
				flag=0
				for p,q in zip(list_a,list_b):
					if ((int(num)==p and i==q) or (i==p and int(num)==q)):
						flag=1
						break
				if flag!=1:
					case=case+1
					list_a.append(int(num))
					list_b.append(i)
	
	return case
	
main()

