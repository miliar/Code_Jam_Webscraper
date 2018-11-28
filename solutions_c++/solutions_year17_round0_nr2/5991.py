#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	long long t;
	cin>>t;
	long long marker;
	for(long long i=0;i<t;i++)
	{
		cin>>s;
		marker=s.size();
		long long j;
		for(j=s.size()-1;j>0;j--)
		{
			if(s[j]<s[j-1])
			{
				s[j-1]--;
				marker=j;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for(j=0;j<s.size()-1 && s[j]=='0' && j<marker;j++);
		for(;j<s.size() && j<marker;j++)
		{
			cout<<s[j];
		}
		for(;j<s.size();j++)
		{
			cout<<"9";
		}
		cout<<endl;
	}
	return 0;
}
