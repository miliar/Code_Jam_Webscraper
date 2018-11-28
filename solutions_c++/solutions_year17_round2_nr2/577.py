#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr, args)

const int maxn = 1e3 + 10;
typedef pair <int, int> pii;

int N;
int a[6];

int dp[maxn][6];

bool cmp (pii x, pii y)
{
	return x.second > y.second;
}

int main ()
{
	freopen ("output.txt", "w", stdout);

	cin.sync_with_stdio (false);
	cin.tie (0);
	cout.tie (0);

	int T;
	cin >> T;

	int test = 0;

	vector <char> C;

	C.push_back ('R');
	C.push_back ('Y');
	C.push_back ('B');
	C.push_back ('G');
	C.push_back ('O');
	C.push_back ('V');

	while (T--)
	{
		cin >> N;

		for (int i = 0; i < 6; ++i)
			cin >> a[i];

		swap (a[2], a[1]);
		swap (a[2], a[4]);

		int zeros = 0;

		zeros += (a[0] == 0);
		zeros += (a[1] == 0);
		zeros += (a[2] == 0);

		for (int i = 3; i < 6; ++i)
			assert (a[i] == 0);

		cout << "Case #" << ++test << ": ";

		if (zeros == 2)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		if (zeros == 1)
		{
			int x = -1;
			int y = -1;

			for (int i = 0; i < 3; ++i)
				if (a[i] != 0)
				{
					if (x == -1)
						x = i;
					else
						y = i;
				}

			if (a[x] != a[y])
			{
				cout << "IMPOSSIBLE\n";
				continue;
			}

			string ans;
			for (int i = 0; i < N; ++i)
			{
				if (i % 2 == 0)
					ans.push_back (C[x]);
				else
					ans.push_back (C[y]);
			}

			assert (ans.size() == N);
			for (int i = 0; i < N; ++i)
				assert (ans[i] != ans[(i + 1) % N] && ans[i] != ans[(i - 1 + N) % N]);

			cout << ans << '\n';
			continue;
		}

		vector <pii> p;
		for (int i = 0; i < 3; ++i)
			p.push_back (pii (i, a[i]));

		sort (p.begin(), p.end(), cmp);

		if (p[1].second + p[2].second < p[0].second)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		int id = 0;

		string ans;

		while (p[0].second)
		{
			ans.push_back (C[p[0].first]);

			if (p[1].second + p[2].second > p[0].second)
			{
				ans.push_back (C[p[1].first]);
				ans.push_back (C[p[2].first]);
				p[2].second--;
				p[1].second--;
			}
			else
			{
				if (p[1].second)
				{
					ans.push_back (C[p[1].first]);
					p[1].second--;
				}
				else
				{
					ans.push_back (C[p[2].first]);
					p[2].second--;
				}
			}

			p[0].second--;
		}

		map <char, int> m;

		assert (ans.size() == N);
		for (int i = 0; i < N; ++i)
			assert (ans[i] != ans[(i + 1) % N] && ans[i] != ans[(i - 1 + N) % N]);

		for (auto i: ans)
			++m[i];

		assert (m['R'] == a[0]);
		assert (m['Y'] == a[1]);
		assert (m['B'] == a[2]);

		cout << ans << '\n';
	}

	return 0;
} 