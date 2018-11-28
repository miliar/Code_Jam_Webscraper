#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ll t;
	cin>>t;
	for(ll it=1;it<=t;it++)
	{
		string s;
		ll k;
		cin>>s>>k;
		ll flip=0;
		cout<<"Case #"<<it<<": ";
		for(ll i=0;i<s.length()-k+1;i++)
		{
			if(s[i]=='-')
			{
				flip++;
				for(ll j=i;j<i+k;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		ll flag=1;
		for(ll i=0;i<s.length();i++)
			if(s[i]=='-')
				flag=0;
		if(flag==0)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<flip<<endl;

	}
	return 0;
}