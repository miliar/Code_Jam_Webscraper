#include <bits/stdc++.h>
typedef int ll;
using namespace std;

int main()
{
	ll t;cin>>t;
	for(ll tc=1;tc<=t;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		string str;cin>>str;
		ll k;cin>>k;
		ll ans=0;
		for(ll i=0;i<=str.length()-k;i++)
		{
			if(str[i]=='-')
			{
				ans+=1;
				for(ll j=i;j<i+k;j++)
				{
					if(str[j]=='+')
						str[j] = '-';
					else
						str[j] = '+';
				}
			}
		}

		int f = 1;
		for(ll i=0;i<str.length();i++)
		{
			if(str[i]=='-')
			{
				f=0;break;
			}
		}

		if(f)
			cout<<ans<<"\n";
		else
			cout<<"IMPOSSIBLE\n";

	}

	return 0;
}