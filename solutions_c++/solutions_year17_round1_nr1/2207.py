#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

char a[30][30];

void solve()
{
	set<int> rproc;
	int n, m;
	int q = 0;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> a[i][j];

	for (int i = 1; i <= n; i++)
	{
		int last = 1;
		for (int j = 1; j <= m; j++)
		{
			if (a[i][j] != '?')
			{
				for (int k = last; k < j; k++)
					a[i][k] = a[i][j];
				last = j + 1;
				rproc.insert(i);
			}
		}

		for (int j = m; j >= last; j--)
			a[i][j] = a[i][last-1];
	}

	queue<pair<int, int>> Q;

	bool proc = true;
	while (proc)
	{
		proc = false;
		for (auto x : rproc)
		{
			if (x + 1 <= n && rproc.find(x + 1) == rproc.end())
			{
				rproc.insert(x + 1);
				Q.push({ x + 1, -1 });
				proc = true;
				break;
			}
			if (x - 1 >= 1 && rproc.find(x - 1) == rproc.end())
			{
				rproc.insert(x - 1);
				Q.push({ x - 1, 1 });
				proc = true;
				break;
			}
		}
	}

	while (!Q.empty())
	{
		auto  i = Q.front();
		Q.pop();
		for (int j = 1; j <= m; j++)
			a[i.first][j] = a[i.first + i.second][j];
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			cout << a[i][j];
		cout << "\n";
	}

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC;
	cin >> TC;
	for (int i = 1; i <= TC; ++i) {
		printf("Case #%d:\n", i);
		solve();
	}

	return 0;
}