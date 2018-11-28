#include <bits/stdc++.h>
using namespace std;
using uint = unsigned int;
using ll = long long;
using pii = pair<int, int>;
#define dbg(x) cerr<<#x": "<<(x)<<'\n'
#define dbg_v(x, n) cerr<<#x"[]: ";for(long long _=0;_<n;++_)cerr<<(x)[_]<<' ';cerr<<'\n'
#define all(v) v.begin(), v.end()
#define NMAX 

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int i, j, k, t, tt, c;
	int v[25];
	ll n;
	bool ok;

	cin >> t;
	for(tt = 1; tt <= t; ++tt)
	{
		cin >> n;
		for(i = 0; n; ++i, n /= 10) v[i] = n % 10;
		k = i;
		reverse(v, v + k);

		for(c = 0, i = 0; i < k; ++i)
		{
			// tb sa pun cel putin v[i]
			for(ok = true, j = i + 1; j < k; ++j)
			{
				if(v[j] < v[i]) { ok = false; break; }
				else if(v[j] > v[i]) break;
			}

			if(!ok)
			{
				v[i] = v[i] - 1;
				for(j = i + 1; j < k; ++j) v[j] = 9;
				break;
			}
		}

		cout << "Case #" << tt << ": ";

		for(i = 0; i < k && !v[i]; ++i);
		for(; i < k; ++i)
			cout << v[i];
		cout << '\n';
	}

	return 0;
}