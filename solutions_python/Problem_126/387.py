t=input();
for h in range(t):
	temp=raw_input();
	temp=temp.split();
	L=temp[0];
	n=int(temp[1]);
	Llen=len(L);
	count=0;
	for i in range(Llen+1):
		for j in range(i+1,Llen+1):
			word=L[i:(j)];
			wlen=len(word);
			cou=0;
			for k in word:
				if(k=='a'or k=='e'or k=='i'or k=='o'or k=='u') :
					cou=0;
				else :
					cou+=1;
				if cou>=n:
					count+=1;
					break;
	print "Case #"+str(h+1)+": "+str(count);
