#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int i=1; i<=t; i++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int count=0;
		
		for(int j=0; j<s.size()-k+1; j++)
		{
			if(s[j] == '-')
			{
				count++;
				for(int p=j; p<j+k; p++)
				{
					if(s[p]=='+')
					{
						s[p]='-';
					}
					else
					{
						s[p]='+';
					}
				}
			}
		}
		
			int flag=0;
			for(int j=0; j<s.size(); j++)
			{
				if(s[j]=='-')
				{
					flag=1;
				}
			}
			
			cout<<"Case #"<<i<<": ";
			if(flag==0)
			{
				cout<<count<<endl;
			}
			else
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
	}
	return 0;
}
