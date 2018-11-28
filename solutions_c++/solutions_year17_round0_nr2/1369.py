#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cout<<"Case #"<<i<<": ";
		string s;
		cin>>s;
		if(s.size()==1)
		{
			cout<<s<<"\n";
			continue;
		}
		for(int j=s.size()-2;j>=0;j--)
		{
			if(s[j]>s[j+1])
			{
				s[j]-=1;
				for(int k=j+1;k<s.size();k++)
					s[k]='9';
			}
		}
		if(s[0]!='0')
			cout<<s[0];
		for(int j=1;j<s.size();j++)
			cout<<s[j];
		cout<<"\n";
	}
	return 0;
}