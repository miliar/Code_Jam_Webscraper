#include<iostream>
#include<string.h>
using namespace std;
main()
{
	int T,K,len,n,flag,count;
	char S[1000];
	cin>>T;
	for(int i=0;i<T;i++)
	{
		flag=0;
		count=0;
		cin>>S;
		cin>>K;
		len=strlen(S);
		for(int j=0;j<len-K+1;j++)
		{
			if(S[j]=='-')
			{
				n=j;
				count++;
				for(;n<j+K;n++)
				{
					if(S[n]=='-')
					S[n]='+';
					else
					S[n]='-';
				}
			}
		}
		for(int j=0;j<len;j++)
		{
			if(S[j]=='-')
			flag=1;
		}		
		if(flag==1)
		cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
