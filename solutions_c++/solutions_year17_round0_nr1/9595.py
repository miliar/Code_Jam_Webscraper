#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,K,i,j,k;
	cin>>T;
	int f=0;
	while(T--)
	{
		f++;
		string S;
		cin>>S>>K;
		int cnt=0;
		
		for(i=0;i<S.size();i++)
		{
			if(S[i]=='-')
			{
				for(j=i;j<i+K && i+K<=S.size();j++)
				{
					if(S[j]=='-')
					S[j]='+';
					else 
					S[j]='-';
				}
				cnt++;
			}	
		}
		int flag=1;
		
		for(i=0;i<S.size();i++)
		{
			if(S[i]=='-')
			flag=0;
		}
		
		if(!flag)
		{
			cout<<"Case #"<<f<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else
		{
		cout<<"Case #"<<f<<": "<<cnt<<"\n";
	    }
	}	
	return 0;
}
