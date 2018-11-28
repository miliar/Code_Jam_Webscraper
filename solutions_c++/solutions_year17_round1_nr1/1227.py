#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long ll;
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;

int m, n;
char ch;

void solve(int nn)
{
	queue <pair <char, int>> q[30];
	char ans[30][30];
	vector <int> emptys;
	bool empty[30];
	int first, last;
	bool flag = false;
	fill(empty, empty + 30, false);
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> ans[i][j];
			if (ans[i][j] != '?')
			{
				if (!flag)
				{
					flag = true;
					first = i;
				}
				q[i].push({ ans[i][j], j });
				ch = ans[i][j];
				last = i;
			}
				
		}
		if (q[i].empty())
			empty[i] = true;
		else
			q[i].push({ ch, m });
	}

	for (int i = 1; i <= n; i++)
	{
		int cur = 1;
		while (!q[i].empty())
		{
			auto p = q[i].front();
			q[i].pop();
			while (cur <= p.second)
			{
				ans[i][cur] = p.first;
				cur++;
			}
		}
	}

	for (int i = first - 1; i > 0; i--)
	{
		for (int j = 1; j <= m; j++)
			ans[i][j] = ans[i + 1][j];
		empty[i] = false;
	}

	for (int i = last + 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
			ans[i][j] = ans[i - 1][j];
		empty[i] = false;
	}


	for (int i = 1; i <= n; i++)
	{
		if (empty[i] && i > 1)
		{
			for (int j = 1; j <= m; j++)
				ans[i][j] = ans[i - 1][j];
		}
	}

	cout << "Case #" << nn + 1 << ": ";
	cout << endl;

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cout << ans[i][j];
		}
		cout << endl;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}