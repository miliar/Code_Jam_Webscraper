#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

ll cnt(ll x)
{
	ll k = 0;
	while (x > 0)
	{
		k++;
		x /= 10;
	}
	return k;
}

ll sol(ll n)
{
	ll ans, p, q, k, cur, res;
	ans = 0;
	cur = 0;
	k = cnt(n);
	p = k;
	q = pow(10, k - 1);
	while (p > 0)
	{
		cur = ans;
		while (cur <= n)
		{
			ans = cur;
			if ((cur / q) % 10 == 9)
			{
				break;
			}
			res = 1;
			for (int i = 0; i < p; i++)
			{
				cur += res;
				res *= 10;
			}
		}
		p--;
		q /= 10;
	}
	return ans;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	ll t, n;
	cin >> t;
	for (int cas = 1; cas <= t; cas++)
	{
		cin >> n;
		cout << "Case #" << cas << ": ";
		cout << sol(n) << endl;
	}
	return 0;
}