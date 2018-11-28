#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		long long int k,count=0,y=-1;
		cin>>s>>k;
		long long int l=strlen(s.c_str());
		for(long long int j=0;j<l;j++)
		{
			if(s[j]=='-' && j<l-k+1)
			{
				count++;
				s[j]='+';
				for(long long int m=j+1;m<j+k;m++)
				{
					if(s[m]=='-' && m<l)
						s[m]='+';
					else if(j<l)
						s[m]='-';
				}
			}
			if(j>l-k && s[j]=='-')
			{
				y=j;
				break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(y==-1)
			cout<<count<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
}
