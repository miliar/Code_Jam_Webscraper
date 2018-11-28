#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <fstream>
#include <unordered_map>
#include <map>
#include <iterator>
#include <iomanip>
#include <stack>
#include <math.h>
#include <bitset>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;

#define TASK "grants"
#define X first
#define Y second
#define mp make_pair
#define inb push_back
#define INF 2e9
#define LINF 9e18
#define eps 1e-6
#define y1 dfsdfsd

const int M = 105;
int n, q, v, u;
vector<pair<int, double> > g[M];
pii e[M];
int c[M][M];
double d[M], dp[M];
bool us[M];

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int p = 1; p <= t; ++p)
	{
		cin >> n >> q;
		for (int i = 1; i <= n; ++i) cin >> e[i].X >> e[i].Y, g[i].resize(0);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
			{
				cin >> c[i][j];
				if (c[i][j] != -1)
					g[i].inb({ j, c[i][j] });
			}
		cout << "Case #" << p << ": ";
		for (; q > 0; --q)
		{
			cin >> v >> u;
			for (int i = 1; i <= n; ++i) d[i] = LINF, us[i] = 0;
			d[v] = 0;
			set<pair<double, int> > q;
			q.insert({ 0, v });
			while(q.size())
			{
				pair<double, int> a = *q.begin();
				q.erase(a);
				set<pair<double, int> > s;
				for (int i = 1; i <= n; ++i) dp[i] = LINF;
				dp[a.Y] = a.X;
				s.insert(a);
				while (s.size())
				{
					pair<double, int> b = *s.begin();
					s.erase(b);
					for (int i = 0; i < g[b.Y].size(); ++i)
					{
						if (g[b.Y][i].Y + (b.X - d[a.Y]) * e[a.Y].Y <= e[a.Y].X && b.X + g[b.Y][i].Y / e[a.Y].Y < dp[g[b.Y][i].X])
						{
							s.erase({ dp[g[b.Y][i].X], g[b.Y][i].X });
							dp[g[b.Y][i].X] = b.X + g[b.Y][i].Y / e[a.Y].Y;
							s.insert({ dp[g[b.Y][i].X], g[b.Y][i].X });
						}
					}
				}
				for(int i = 1; i <= n; ++i) 
					if (i != a.Y && dp[i] < d[i])
					{
						q.erase({ d[i], i });
						d[i] = dp[i];
						q.insert({ d[i], i });
					}
			}
			cout.precision(9);
			cout << fixed << d[u] << ' ';
		}
		cout << '\n';
	}
}