


if __name__=='__main__':
	Test_Num = int(input().strip());
	for i in range(Test_Num):
		tmp = input().strip().split(' ');
		des = int(tmp[0]);
		num = int(tmp[1]);
		maxv = 0;
		for j in range(num):
			tmp = input().strip().split(' ');
			val = (des-int(tmp[0]))/int(tmp[1]);
			maxv = max(maxv,val);

		print('Case #'+str(i+1)+': '+str(des/maxv));


