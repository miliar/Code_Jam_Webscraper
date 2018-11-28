#include <bits/stdc++.h>

using namespace std;
typedef long double ll;
#define BR __int("$3");

pair<ll, ll> pa[1001];
int n;
int k;
ll res;
ll res2;
ll ma;
const long double pi = 3.14159265358979323846l;
#define h first
#define r second

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
		{
			cin >> pa[i].r >> pa[i].h;
			pa[i].h *= pa[i].r * 2.0;
		}
		sort(pa, pa + n);
		res = 0;
		ma = 0;
		for (int i = n - 1; i > n - k; --i)
		{
			res += pa[i].h;
			ma = max(ma, pa[i].r * pa[i].r);
		}
		res2 = res + pa[n - k].h + max(ma, pa[n-k].r * pa[n-k].r);
		for (int i = n - k - 1; i >= 0; --i)
		{
			res2 = max(res2, res + pa[i].h + max(ma, pa[i].r * pa[i].r));
		}
		cout << setprecision(7) << fixed;
		cout << "Case #" << tt << ": " << pi * res2 << endl;
	}

	return 0;
}
