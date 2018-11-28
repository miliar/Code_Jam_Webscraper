#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		cout<<"Case #"<<i<<": ";
		int j;
		int count=0;
		for(j=0;j<=s.length()-k;j++)
		{
			if(s[j]=='-')
		
		{
			for(int f=j;f<j+k;f++)
			{
				if(s[f]=='-')
				s[f]='+';
				else
				s[f]='-';
			}
			
			count++;
		
		
		
	}
	
	}
	int flag=0;
	for(int j=0;j<s.length();j++)
	{
		if(s[j]=='-')
		flag=1;
		
	}
	if(!flag)
	cout<<count<<" \n";
	else
	cout<<"IMPOSSIBLE"<<"\n";
		
	}
}
