# the function to calculate the GCD
def gcd(n, d):
	while d != 0:
		t = d
		d = n%d
		n = t
	return n

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

for n in range(len(ipt)):
	ipt[n] = ipt[n][:-1]

res = []

n=1
while n<len(ipt):
	a=ipt[n].split()
	b=ipt[n+1].split()
	
	if a[1]<="1" and a[2]>="1":
		res.append(1)
		n+=2
		continue
		
	r=1
	for i in b:
		r=lcm(r,int(i))
	
	s=0
	for i in range(int(a[1]),int(a[2])+1):
		aa=[]
		for j in b:
			if i%int(j) == 0 or int(j)%i == 0:
				aa.append(1)
		if len(aa) == len(b):
			s=1
			res.append(i)
			break
	
	if s==0:
		res.append("NO")
		
	n+=2
	
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ": " + str(res[n]) + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")