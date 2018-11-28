if __name__ == '__main__':
	from functools import reduce
	n = int(input())
	for k in range (0,n):

		a=int(input())
		b=list(map(int, str(a)))
		last_less=0
		i=-1
		le=len(b)
		flag=1
		for i in range (0,le-1):
			if (b[i]<=b[i+1]):
				if(b[i]<b[i+1]):
					last_less = i+1
			else:
				flag = 0
				break
		if (flag != 1):
			if (b[last_less]==1):
				del b[-1]
			else:
				b[last_less]-=1
				last_less+=1
			for j in range (last_less , len(b)):
				b[j]=9
			
		c = reduce(lambda x,y: x+str(y), b, '')
		num = int(c)
		print("Case #%d: %d" % (k+1,num))    
