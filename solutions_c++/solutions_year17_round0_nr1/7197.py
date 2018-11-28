#include<bits/stdc++.h>
#define ll long long int
using namespace std;
string str;
void flip(ll i)
{
	if(str[i]=='+')
	{
		str[i]='-';
	}
	else
	{
		str[i]='+';
	}
}
bool chek()
{
	for(ll i=0;i<str.length();i++)
	{
		if(str[i]=='-')
		{
			return false;
		}
	}
	return true;
}
int main()
{
	freopen("inpl.in","r",stdin);
    freopen("outl.in","w",stdout);
	ios::sync_with_stdio(false);
	ll t,te=1;
	cin>>t;
	while(te<=t)
	{
		ll ans=0,k,n;
		str.clear();
		cin>>str;
		cin>>k;
		n=str.length();
		ll i=0;
		while(i<=(n-k))
		{
			if(str[i]=='-')
			{
				ans++;
				for(ll j=i;j<k+i;j++)
				{
					flip(j);
				}
			}
			i++;
		}
		if(chek())
		{
			cout<<"Case #"<<te<<": "<<ans<<"\n";
		}
		else
		{
			cout<<"Case #"<<te<<": IMPOSSIBLE\n";
		}
		te++;
	}
}
