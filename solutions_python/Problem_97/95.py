

def switch(s):
	return s[-1] + s[:-1]



if __name__=='__main__':
	
	f = open('C-large.in','r')
	f1 = open('C.out','w')
	
	T = int(f.readline())
	for case in range(T):
		nums = f.readline().split()
		a = int(nums[0])
		b = int(nums[1])
		ans = 0
		for k in range(a,b+1):
			s = str(k)
			d = []
#			print k
			for i in range(len(str(k))-1):
				s = switch(s)
#				print '  ' + str(s)	
				if (int(s)>k and int(s)<=b):
#					print k,
#					print '   '+ s
					if s not in d:
						d.append(s);	
						ans = ans + 1;
					

		f1.write('Case #%d: %d\n'%((case+1),ans))
			
	


	f.close()
	f1.close()
