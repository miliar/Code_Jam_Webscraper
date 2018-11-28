#include <bits/stdc++.h>

using namespace std;

const int maxn = 51;

bool check(int q, int num)
{
	return num * 9 <= q * 10 && q * 10 <= num * 11;
}
bool match(pair<int, int> a, pair<int, int> b)
{
	if (a.first > b.first)
		swap(a, b);
	return a.first <= b.first && b.first <= a.second;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int n, p, ans = 0;
		int R[maxn];
		vector<pair<int, int> > v[maxn];
		printf("Case #%d: ", t);
		cin >> n >> p;
		for (int i = 0; i < n; ++i)
			cin >> R[i];
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < p; ++j)
			{
				int q, l, r;
				cin >> q;
				l = max(1, 10 * q / (11 * R[i]));
				r = 10 * q / (9 * R[i]);
				if (!check(q, R[i] * l))
					++l;
				// cout << l << ' ' << r << endl;
				if (l <= r)
					v[i].push_back(make_pair(l, r));
			}
			sort(v[i].begin(), v[i].end());
		}
		int j[maxn];
		for (int i = 0; i < n; ++i)
			j[i] = 0;
		for (auto it : v[0])
		{
			int cnt = 1;
			for (int i = 1; i < n; ++i)
			{
				while (j[i] < v[i].size() && v[i][j[i]].first < it.first && !match(v[i][j[i]], it))
					++j[i];
				if (j[i] != v[i].size() && match(v[i][j[i]], it))
					++cnt;
			}
			if (cnt == n)
			{
				++ans;
				for (int i = 1; i < n; ++i)
					++j[i];
			}
		}
		cout << ans << endl;
	}
}
 
