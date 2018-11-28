#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(int argc, char const *argv[])
{
	ll t;
	cin>>t;
	for (ll x = 1; x <= t; ++x)
	{
		ll n,k;
		cin>>n>>k;
		ll count = 0;
		map<ll, ll> ma;
		ma[n] = 1;
		// ma.erase(n);
		// cout<<ma.begin()->first<<" "<<ma.begin()->second;

		while(count < k)
		{
			ll temp = ma.rbegin()->second;
			if(count + temp < k)
			{
				ll number = ma.rbegin()->first;
				number = number - 1;
				ll one,two;
				if(number%2 == 0)
				{
					one = number/2;
					two = number/2;
				}
				else
				{
					one = number/2 + 1;
					two = number/2;
				}
				ma[one] += temp;
				ma[two] += temp;
				ma.erase(number+1);
				// cout<<number<<"\n";
				count = count + temp;
			}
			else
			{
				ll ans = ma.rbegin()->first;
				// cout<<ans<<"\n";

				if(ans == 1 || ans == 0)
				{
					cout<<"Case #"<<x<<": 0 0\n";
				}
				else
				{
					ans = ans-1;
					ll one,two;
					if(ans%2 == 0)
					{
						one = ans/2;
						two = ans/2;
					}
					else
					{
						one = ans/2 + 1;
						two = ans/2;
					}
					cout<<"Case #"<<x<<": "<<one<<" "<<two<<"\n";
				}
				break;
			}
		}

	}
	return 0;
}