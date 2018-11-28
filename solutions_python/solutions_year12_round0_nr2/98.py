

if __name__=='__main__':
	f = open('B-large.in','r')
	f1 = open('B.out','w')
	T = int(f.readline())
	for case in range(T):
		nums = f.readline().split()
		n = int(nums[0])
		s = int(nums[1])
		p = int(nums[2])
		score = [int(item) for item in nums[3:]]
		
		ans = 0;
		for i in range(n):
			tmp = score[i];
			tmp = tmp - p - max(0,(p-1))*2;
			if tmp>=0:
				ans=ans+1;
			else:
				if (s>0 and score[i]-p-max(0,(p-2))*2>=0):
					s = s-1;
					ans = ans+1;

		f1.write('Case #%d: %d\n' % ((case+1),ans))

		

	f.close()
	f1.close()
