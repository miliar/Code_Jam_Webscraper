#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

pair <ll, ll> res;

void sol(ll n, ll k)
{
	multiset <ll, greater<ll>> h;
	ll f, r, kol = 0;
	h.insert(n);
	for (int i = 0; i < k - 1; i++)
	{
		f = *h.begin();
		h.erase(h.begin());
		r = (f - 1) / 2;
		h.insert(r);
		if (f & 1)
		{
			h.insert(r);
		}
		else
		{
			h.insert(r + 1);
		}
	}
	f = *h.begin();
	r = (f - 1) / 2;
	if (f % 2 == 1)
	{
		res.first = r;
	}
	else
	{
		res.first = r + 1;
	}
	res.second = r;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	ll t, n, k;
	cin >> t;
	for (int cas = 1; cas <= t; cas++)
	{
		cin >> n >> k;
		cout << "Case #" << cas << ": ";
		sol(n, k);
		cout << res.first << " " << res.second << endl;
	}
	return 0;
}