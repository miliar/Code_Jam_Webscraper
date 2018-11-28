#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll n, k;

int main()
{
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> n >> k;
		map<ll, ll> pq;
		pq[n] = 1;
		while (k)
		{
			ll s, c;
			tie(s, c) = *pq.rbegin();
			pq.erase(s);
			ll l = (s - 1) / 2, r = s / 2;
			if (c >= k)
			{
				cout << "Case #" << C << ": " << r << ' ' << l << '\n';
				break;
			}
			if (l != 0) pq[l] += c;
			if (r != 0) pq[r] += c;
			k -= c;
		}
	}
	return 0;
}
