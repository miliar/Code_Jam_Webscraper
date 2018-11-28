#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;

void solve(ll l1, ll c1, ll l2, ll c2, ll k)
{
	if (c2 >= k)
	{
		ll mid = l2 / 2;
		printf("%lld %lld\n", max(mid, l2 - mid - 1), min(mid, l2 - mid - 1));
		return;
	}
	k -= c2;
	if (c1 >= k)
	{
		ll mid = l1 / 2;
		printf("%lld %lld\n", max(mid, l1 - mid - 1), min(mid, l1 - mid - 1));
		return;
	}
	k -= c1;

	ll l11 = l1 / 2;
	ll l12 = max(0LL, l1 - l11 - 1);

	ll l21 = l2 / 2;
	ll l22 = max(0LL, l2 - l21 - 1);
	map <ll, ll> occ = {};
	occ[l11] += c1;
	occ[l12] += c1;

	occ[l21] += c2;
	occ[l22] += c2;

	vector <pair<ll, ll>> result = {};
	for (auto x : occ)
	{
		if (x.first != 0)
			result.push_back(x);
	}
	sort(result.begin(), result.end());
	assert (occ.size() != 0);

	if (result.size() == 1)
		solve(0, 0, result[0].first, result[0].second, k);
	else
		solve(result[0].first, result[0].second, result[1].first, result[1].second, k);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		ll n, k;
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", i + 1);
		solve(0, 0, n, 1, k);
	}
	return 0;
}
