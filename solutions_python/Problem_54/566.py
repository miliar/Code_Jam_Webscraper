
def gcd(x,y):
	if x>y:
		t=x
		x=y
		y=t
	while (y!=0):
		t=x%y
		x=y
		y=t
	return x

def work():
	s=tf.readline()
	t=s.find(' ')
	num=int(s[0:t])
	s=s[t+1:]
	ls=[]
	for i in range(0,num-1):
		t=s.find(' ')
		ls.append(int(s[0:t]))
		s=s[t+1:]
	ls.append(int(s))
	ans=abs(ls[num-1]-ls[num-2])
	for i in range(0,num-2):
		t=abs(ls[i]-ls[i+1])
		ans=gcd(ans,t)
	t=ls[0]%ans
	if t==0:
		return 0
	else:
		return ans-t

tf=open("input.txt",'r')
ou=open("output.txt",'w')
CaseNum=int(tf.readline())
for CN in range(0,CaseNum):
	ou.write("Case #"+str(CN+1)+": "+str(work())+'\n')
tf.close()
ou.close()
