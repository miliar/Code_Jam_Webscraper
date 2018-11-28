#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		ll n;
		cin >> n;
		vector<int> v;
		for (ll d = n; d > 0; d /= 10LL)
			v.push_back(d % 10LL);
		reverse(v.begin(), v.end());
		int sz = (int)v.size();
		while (1)
		{
			int f = -1;
			for (int j = 0; j < sz - 1; j++)
				if (v[j] > v[j + 1])
				{
					f = j;
					break;
				}
			if (f == -1)
				break;
			v[f]--;
			for (int j = f + 1; j < sz; j++)
				v[j] = 9;
		}
		ll ans = 0;
		for (int j = 0; j < sz; j++)
			ans = ans * 10LL + (ll)v[j];
		cout << "Case #" << (q + 1) << ": " << ans << "\n";
	}
	return 0;
}