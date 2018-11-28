#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int r=1;r<=t;r++)
	{
		string s;
		int k,i;
		cin>>s>>k;
		for(i=0;i<s.size();i++)
		{
			if(s[i]=='-')
				break;
		}
		long long int count=0;
		while(s[i]=='-'&&k+i-1<s.size())
		{
			count++;
			for(int j=i;j<k+i;j++)
			{
				if(s[j]=='-')
					s[j]='+';
				else
					s[j]='-';
			}
			for(int t=i;t<s.size();t++)
			{
				if(s[t]=='-')
				{
					i=t;
					break;
				}
			}
		}
		cout<<"Case #"<<r<<": ";
		if(i<s.size() && s[i]=='-')
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
			cout<<count<<endl;
		
	}
	return 0;
}