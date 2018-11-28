#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int T = 0; T < t; T++)
	{
		cout << "Case #" << T+1 << ": ";
		ll n, k;
		cin >> n >> k;
		map<ll, ll> mp;
		mp[n] = 1;
		while (true)
		{
			auto p = *mp.rbegin();
			mp.erase(p.first);
			if (k <= p.second)
			{
				cout << p.first / 2 << " " << (p.first - 1) / 2 << "\n";
				break;
			}
			else
			{
				k -= p.second;
				mp[p.first / 2] += p.second;
				mp[(p.first - 1) / 2] += p.second;
			}
		}
	}


	return 0;
}
