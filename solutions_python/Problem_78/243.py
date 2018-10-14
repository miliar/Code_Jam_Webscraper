
def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result


f=open('fc.in','r')
cases= f.readline()


for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":",
	array = f.readline().split(" ")
	intarray = [int(x) for x in array]

	n=intarray[0]
	a=intarray[1]
	b=intarray[2]

	flag=0
	mingames=-1
	if (a<100 and b==100) or (a>0 and b==0):
		flag=1

	elif a>0:
		mingames = 100/gcd(a,100);
		if mingames > n :
			flag=1


	if flag==0:
		print "Possible"
	else:
		print "Broken"



