#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 100500;

void print_ans(ll x)
{
	printf("%lld %lld\n", x / 2, (x - 1) / 2);
}

void sol()
{
	ll n, k;
	scanf("%lld%lld", &n, &k);
	map <ll, ll> pl;
	
	pl[n] = 1;
	k--;	

	while (pl.rbegin()->second <= k)
	{
		ll x = pl.rbegin()->first;
		ll cnt = pl.rbegin()->second;
		//cout << x << ' ' << cnt << ' ' << k << '\n';
		k -= cnt;
		pl.erase(pl.find(x));
		pl[x / 2] += cnt;
		pl[(x - 1) / 2] += cnt;
	}
	print_ans(pl.rbegin()->first);
}

int main()
{                                                     
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		sol();
	}
	return 0;
}

