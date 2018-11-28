#include<bits/stdc++.h>
using namespace std;
char S[1005];

int main()
{
	freopen("testcase.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int flag=0;
	long int T,N,K;
	cin>>T;
	for(int j=1;j<=T;j++)
	{
		flag=0;
		N=0;
		cin>>S>>K;
		long int L=strlen(S);
		for(int i=0;i<L-K+1;i++)
		{
			if(S[i]=='-')
			{
				N++;
				S[i]='+';
				for(int k=i+1;k<i+K;k++)
				{
					if(S[k]=='+')
						S[k]='-';
					else
						S[k]='+';
				}
			}
		}
		
		for(int i=0;i<L;i++)
		{
			if(S[i]=='-')
				flag=1;
		}
		
		if(flag==0)
		{
			cout<<"Case #"<<j<<": "<<N<<endl;
		}
		
		else
		{
			cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
}
