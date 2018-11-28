#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,sum=0,d,a,b,c,n,i,j,K;
	cin>>t;
	string S;
	for(i=1;i<=t;i++)
	{
		cin>>S>>K;
		c=0;b=0;d=0;sum=0;
		n=S.length();
		while(d<n)
		{
			//cout<<"d=="<<d<<" s[d]=="<<S[d]<<endl;
			if(S[d]=='-')
			{
				sum++;
				for(j=d;d+K<=n && j<d+K;j++)
				{
					if(S[j]=='-')
					{
						S[j]='+';
					}
					else
					{
						S[j]='-';
					}
					//cout<<"s[j]=="<<S[j]<<endl;
					//cout<<"dd=="<<d<<endl;
				}
				if(d+K>n)
				{
					d=n;
				}
			}
			d++;
		}
		for(j=0;j<n;j++)
		{
			if(S[j]=='-')
			{
				c=1;
				break;
			}
		}
		if(c==1)
		{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}
			
	}
	
}
