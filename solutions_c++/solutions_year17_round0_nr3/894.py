#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
int t;
ll n,k;
map<pll, ll> dpmin;
map<pll, ll> dpmax;
ll solvemin(ll n, ll k)
{
	if (k == 1)
	{
		if (n <= 0)
			return 0;
		if (n%2 == 0)
			return n/2 - 1;
		else
			return n/2;
	}
	else if (k <= 0)
	{
		return n;
	}
	else if (n <= 0)
	{
		return 1000000000000000000LL;
	}
	if (dpmin.count(make_pair(n, k)))
		return dpmin[make_pair(n, k)];
	ll & ret = dpmin[make_pair(n, k)];
	k--;
	if (n%2 == 1)
		return ret = min(solvemin(n/2, k/2), solvemin(n/2, (k + 1)/2));
	else
	{
		ret = min(solvemin(n/2 - 1, k/2), solvemin(n/2, (k + 1)/2));
		return ret;
	}
}

ll solvemax(ll n, ll k)
{
	if (k == 1)
	{
		if (n <= 0)
			return 0;
		return n/2;
	}
	else if (k <= 0)
	{
		return n;
	}
	else if (n <= 1)
	{
		return 1000000000000000000LL;
	}
	if (dpmax.count(make_pair(n, k)))
		return dpmax[make_pair(n, k)];
	ll & ret = dpmax[make_pair(n, k)];
	k--;
	if (n%2 == 1)
		return ret = min(solvemax(n/2, k/2), solvemax(n/2, (k + 1)/2));
	else
	{
		ret = min(solvemax(n/2 - 1, k/2), solvemax(n/2, (k + 1)/2));
		return ret;
	}
}

int main(void)
{
	ios :: sync_with_stdio(false);
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> k;
		dpmin.clear();
		dpmax.clear();
		cout << "Case #" << i << ": " << solvemax(n, k) << " " << solvemin(n, k) << "\n";
	}
	return 0;
}
