n=input();
i=1;
while(i<=n):
	print "Case #%d:"%(i),
	ma=[]
	k=input();
	while(k):
		ma.append(k%10);	
		k/=10;
	ma.reverse();
	temp=[]
	for za in ma:
		temp.append(za);
	temp.sort();
	flag=0;
	j=0;
	x=len(ma);
	while(j<x):
		if(temp[j]<ma[j]):
			k=j+1;
			min=100;
			index=-1;
			while(k<x):
				if(temp[k]>=ma[j]):
					if(min>temp[k]):
						min=temp[k];
						index=k;
				k=k+1;
			if(index is not -1):
				za = temp[j];
				temp[j] = temp[index];
				t1=temp[j+1:index];
				t2=temp[index+1:];
				v=[za];
				temp[j+1:]=v+t1+t2;
				if(temp[j]>ma[j]):
					flag = 1;
					break;
		j=j+1;
	if(flag):
		print temp;
		p=0;
		ans="";
		while(p<x):
			ans=ans+str(temp[p]);
			p=p+1;
		print ans;
	else:
		p=0;
		ans = 10**21;
		while(p<x):
			k=p+1;
			index=-1;
			min=100;
			while(k<x):
				if(temp[k]>temp[p]):
					if(min>temp[k]):
						min=temp[k];
						index=k;
				k=k+1;
			if(index!=-1):
				newlist=temp[0:p];
				newlist.append(min);
				k=p;
				arr=[]
				while(k<x):
					if(k!=index):
						arr.append(temp[k]);
					k=k+1;
				arr.sort();
				for madh in arr:
					newlist.append(madh);
				num=0;
				for z in newlist:
					num=num*10+z;
				if(ans>num):
					ans=num;
			p=p+1;
		if(ans!=10**21):
			print ans;
		else:
			temp.sort();
			p=0;
			while(temp[p]==0):
				p=p+1;
			arr=[temp[p]];
			arr.append(temp[0:p]);
			arr.append(0);
			arr.append(temp[p+1:]);
			ans=0;
			for p in arr:
				try:
					ans=ans*10+p;
				except:
					for z in p:
						ans=ans*10+z;
			print ans;				
		i=i+1;
