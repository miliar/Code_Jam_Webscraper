#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll,ll> pp;
#define pb push_back
#define faster ios_base::sync_with_stdio(0);cin.tie(0)
ll dig(ll n)
{
	ll temp = n,d=0;
	while(temp)
	{
		d++;
		temp/=10;
	}
	return d;
}
ll number(ll d)
{
	if(d==1)
		return 0;
	if(d==2)
		return 9;
	ll num=0;
	for(ll i=0;i<d-1;i++)
	{
		num+=(9)*pow(10, i);
		// cout<<"num="<<num<<"\n";
	}
	return num;
}
bool check(ll num)
{
	int x,c;
	x = num%10;
	num/=10;
	bool f=1;
	while(num)
	{
		c = num%10;
		if(c>x)
		{
			f=0;
			break;
		}
		x = c;
		num/=10;
	}
	return f;
}
int main()
{
	// faster;
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int t;
	ll i,n,maxi=-1;
	cin>>t;
	// t=1;
	for(ll j=1;j<=t;j++)
	{
		ll ans;
		cin>>n;
		// ll digits = dig(n);
		// cout<<"digits="<<digits<<"\n";
		// ll num = number(digits);
		// cout<<"num="<<num<<"\n";
		// for(;num<=n;num++)
		// {
		// 	if(check(num))
		// 	{
		// 		ans = num;
		// 	}
		// }
		for(i=n;i>=0;i--)
		{
			if(check(i))
			{
				ans=i;
				break;
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<"\n";
	}
	return 0;
}
