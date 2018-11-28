#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
	ll t;
	cin>>t;
	for(ll p=1;p<=t;p++)
	{
		ll ans=0;
		string s;
		cin>>s;
		ll n=s.size();
		ll k;
		cin>>k;
		for(ll i=0;i<n-k+1;i++)
		{
			if(s[i]=='+') continue;
			else
			{
				for(ll j=0;j<k;j++)
				{
					if(s[i+j]=='+') s[i+j]='-';
					else 
					{
						s[i+j]='+';
					}
				}
				ans++;
			}
		}
		bool flag=true;
		for(ll i=n-k;i<n;i++)
		{
			if(s[i]=='-') flag=false;
		}
		if(flag)
		cout<<"Case #"<<p<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<p<<": IMPOSSIBLE\n";
	}
	return 0;
}
