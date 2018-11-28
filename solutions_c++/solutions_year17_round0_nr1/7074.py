#include<bits/stdc++.h>
using namespace::std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		string s;
		int k;
		cin>>s>>k;
		int co=0;
		int l = s.length();
		l=l-k+1;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				co++;
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='+')
						s[i+j]='-';
					else
						s[i+j]='+';
				}
			}
		}
		int minus=0;
		for(unsigned int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				minus=1;
				break;
			}
		}
		if(minus)
			cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<c<<": "<<co<<endl;
	}
	return 0;
}
