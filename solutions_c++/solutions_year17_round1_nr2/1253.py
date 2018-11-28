#include <math.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int fac(int n)
{
	if (n < 1)
		return 1;
	return n * fac(n - 1);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int _case = 1; _case <= cases; _case++)
	{
		int n, p;
		cin >> n >> p;

		vector<int> r(n);
		vector<vector<int>> q(n, vector<int>(p));
		vector<vector<pair<int, int>>> range(n);
		for (int i = 0; i < n; i++)
			cin >> r[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++)
				cin >> q[i][j];

		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++)
			{
				auto pii = make_pair(ceil(q[i][j] / (r[i] * 1.1)), floor(q[i][j] / (r[i] * 0.9)));
				// if (pii.first <= pii.second)
				range[i].push_back(pii);
			}

		int ans = 0;
		for (int i = 0; i < fac(p); i++)
		{
			vector<int> a(p), b(p);
			int t = i;
			for (int j = 0; j < p; j++)
			{
				int f = fac(p - j - 1);
				a[j] = t / f;
				t %= f;
			}
			vector<bool> v(p, false);
			for (int j = 0; j < p; j++)
			{
				int k, c = 0;
				for (k = 0; k < p; k++)
					if (!v[k] && a[j]-- == 0)
					{
						b[j] = k;
						v[k] = true;
						break;
					}
			}

			int c = 0;
			for (int j = 0; j < p; j++)
			{
				int mn = n > 1 ? max(range[0][j].first, range[1][b[j]].first) : range[0][j].first;
				int mx = n > 1 ? min(range[0][j].second, range[1][b[j]].second) : range[0][j].second;
				c += (mn <= mx);
			}
			ans = max(ans, c);
		}

		cout << "Case #" << _case << ": " << ans << endl;
	}
	return 0;
}