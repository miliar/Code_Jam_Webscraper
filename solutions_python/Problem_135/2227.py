f=open("a.txt",'w')
def main():

	with open('A-small-attempt1.in', 'r') as f:
		a=f.readlines()
	N=int(a[0])
	for i in range(0,N):
		ch1=a[1+10*i]
		sq1=[a[2+10*i],a[3+10*i],a[4+10*i],a[5+10*i]]
		ch2=a[6+10*i]
		sq2=[a[7+10*i],a[8+10*i],a[9+10*i],a[10+10*i]]
		calc(ch1,sq1,ch2,sq2,i+1)
def calc(ch1,sq1,ch2,sq2,d):
	ch1=int(ch1)
	ch2=int(ch2)
	ch1=ch1-1
	ch2=ch2-1
	l1=[]
	l2=[]	


	for i in range(0,4):
		l1.append(sq1[i].split(' '))
	for i in range(0,4):
		for j in range(0,4):
			l1[i][j]=int(l1[i][j])


	for i in range(0,4):
		l2.append(sq2[i].split(' '))
	for i in range(0,4):
		for j in range(0,4):
			l2[i][j]=int(l2[i][j])
	
	count=0
	variable=-1	
	for i in range(0,4):
		for j in range(0,4):
			if l1[ch1][i]==l2[ch2][j]:
				count=count+1
				variable=l1[ch1][i]
	if count==0:
		f.write("Case #"+str(d)+": "+"Volunteer cheated!"+"\n")
	if count ==1:
		f.write("Case #"+str(d)+": "+str(variable)+"\n")
	if count>1:
		f.write("Case #"+str(d)+": "+"Bad magician!"+"\n")

if __name__ == "__main__":
    main()
