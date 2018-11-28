#include <iostream>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <algorithm>
#define ld long double
#define ll long long
using namespace std;
const ll maxn = 1000;
const ld pi = 4*atan(1);
ll n,k;
ll r[maxn+1],h[maxn+1],id[maxn+1];
ld xq[maxn+1];
ll getbit(ll x,ll n)
{
	return (x>>(n-1) & 1);
}
bool cmp(ll x,ll y)
{
	return xq[x]>xq[y];
}
void solve()
{
	cin >> n >> k;
	for (ll i=1; i<=n; i++)
	{
		cin >> r[i] >> h[i];
		xq[i]=2*r[i]*pi*h[i];
		id[i]=i;
	}
	sort(id+1,id+1+n,cmp);
	ld res=0;
	for (ll i=1; i<=n; i++)
	{
		ld top=r[i]*r[i]*pi;
		ld ben=2*r[i]*pi*h[i];
		ll chosen=0;
		for (ll j=1; j<=n; j++)
		{
			if (id[j]!=i and chosen<k-1)
			{
				chosen++;
				ben+=xq[id[j]];
			}
		}
		res=max(res,top+ben);
	}
	cout << setprecision(10) << fixed << res;
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t;
	cin >> t;
	for (ll i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}