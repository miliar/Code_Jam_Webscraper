#include <bits/stdc++.h>
using namespace std;

char ans[1005];

typedef pair<int, char> colo;

int n, r, o, y, g, b, v;

vector<char> ccc[3];

colo c[6];

void check(int n)
{
	ans[n] = ans[0];
	for (int i = 0; i < n; i++)
	{
		fprintf(stderr, "%d %c %c\n", i, ans[i], ans[i + 1]);
		assert(ans[i] != ans[i + 1]);
	}
	ans[n] = 0;
}

void sol(int cas)
{
	c[0].second = 'R';
	c[1].second = 'O';
	c[2].second = 'Y';
	c[3].second = 'G';
	c[4].second = 'B';
	c[5].second = 'V';
	cin >> n
		>> c[0].first
		>> c[1].first
		>> c[2].first
		>> c[3].first
		>> c[4].first
		>> c[5].first;
	for (int i = 0; i < 6; i++) ccc[i].clear();
	sort(&c[0], &c[6], greater<colo>());
	if (c[0].first * 2 > n)
	{
		printf("Case #%d: IMPOSSIBLE\n", cas);
		return;
	}
	memset(ans, 0, sizeof ans);
	for (int i = 0; i < c[0].first; i++)
		ccc[0].push_back(c[0].second);
	for (int i = 0; i < c[0].first; i++)
	{
		if (c[1].first) {
			ccc[1].push_back(c[1].second);
			c[1].first--;
		} else {
			ccc[1].push_back(c[2].second);
			c[2].first--;
		}
	}
	for (int i = 0; i < c[2].first; i++)
		ccc[2].push_back(c[2].second);
//cout << ccc[0].size() << ' ' << ccc[1].size() << ' ' << ccc[2].size() << endl;
	int tn = n;
	int h[3];
	h[0] = h[1] = h[2] = 0;
	while (n)
	{
	
//	cout << h[0] << ' ' << h[1] << ' ' << h[2] << endl;
		for (int i = 0; i < 3; i++)
		{
			if (ccc[i].size() != h[i])
			{
				ans[--n] = ccc[i][h[i]++];
			}
		}
	}
	check(tn);
	printf("Case #%d: %s\n", cas, ans);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) sol(i);
	return 0;
}
