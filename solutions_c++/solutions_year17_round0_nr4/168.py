#include <bits/stdc++.h>

using namespace std;

const int maxn = 101;
const int c[4] = {'.', 'x', '+', 'o'};

typedef int matrix[maxn][maxn];
int n, m;
matrix origin, ans;
vector<pair<int, int> > m1, m2;

bool check1(int x, int y)
{
	for (auto i: m1)
	{
		int tx = i.first, ty = i.second;
		if (x == tx || y == ty)
			return false;
	}
	return true;
}
bool check2(int x, int y)
{
	if (x < 1 || x > n || y < 1 || y > n)
		return false;
	for (auto i: m2)
	{
		int tx = i.first, ty = i.second;
		if (x + y == tx + ty || x - y == tx - ty)
			return false;
	}
	return true;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		cin >> n >> m;
		char s[2];
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				ans[i][j] = origin[i][j] = 0;
		m1.clear();
		m2.clear();
		for (int i = 0; i < m; ++i)
		{
			int x, y;
			cin >> s >> x >> y;
			if (s[0] == 'x' || s[0] == 'o')
			{
				origin[x][y] += 1;
				m1.push_back(make_pair(x, y));
			}
			if (s[0] == '+' || s[0] == 'o')
			{
				origin[x][y] += 2;
				m2.push_back(make_pair(x, y));
			}
		}

		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (check1(i, j))
				{
					m1.push_back(make_pair(i, j));
					break;
				}
		for (int i = 2; i <= 2 * n; ++i)
		{
			for (int j = 1; j <= i - 1; ++j)
				if (check2(j, i - j))
				{
					m2.push_back(make_pair(j, i - j));
					break;
				}
			i = 2 * n - i + 2;
			for (int j = 1; j <= i - 1; ++j)
				if (check2(j, i - j))
				{
					m2.push_back(make_pair(j, i - j));
					break;
				}
			i = 2 * n - i + 2;
		}

		for (auto i: m1)
			ans[i.first][i.second] |= 1;
		for (auto i: m2)
			ans[i.first][i.second] |= 2;

		int cnt = 0;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				cnt += ans[i][j] != origin[i][j];
		cout << m1.size() + m2.size() << ' ' << cnt << endl;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (ans[i][j] != origin[i][j])
					printf("%c %d %d\n", c[ans[i][j]], i, j);
	}
}
