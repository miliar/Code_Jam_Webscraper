/*
СТРОИМ СТЕНУ РАБОТЯГИ!
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)

char a[57][57];
int n, m;
bool was[57][57][4];
int id[57][57];
bool ok[57][57][2];
vector<pair<int, int> > pts;
int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
vector<pair<int, int> > can[57][57];
vector<pair<int, int> > g[2507][2], rg[2507][2];
void addEdge(pair<int, int> a, pair<int, int> b)
{
//	cerr << "EDGE: " << a.fi << " " << a.se << " " << b.fi << " " << b.se << endl;
	g[a.fi][a.se].push_back(b);
	rg[b.fi][b.se].push_back(a);
}
void dfs(int x, int y, int dir)
{
	if (was[x][y][dir]) return;
	if (x <= 0 || x > n || y <= 0 || y > m) return;
	if (a[x][y] == '#') return;
	pts.push_back(make_pair(x, y));
	if (a[x][y] == '-' || a[x][y] == '|')
	{
		return;
	}
	if (a[x][y] == '.')
	{
		dfs(x + dx[dir], y + dy[dir], dir);
	}
	else if (a[x][y] == '\\')
	{
		int goDir = dir;
		if (dir == 0)
		{
			goDir = 1;
		}
		else if (dir == 1)
		{
			goDir = 0;
		}
		else if (dir == 2)
		{
			goDir = 3;
		}
		else
		{
			goDir = 2;
		}
		dfs(x + dx[goDir], y + dy[goDir], goDir);
	}
	else
	{
		int goDir = dir;
		if (dir == 0)
		{
			goDir = 0;
		}
		else if (dir == 1)
		{
			goDir = 2;
		}
		else if (dir == 2)
		{
			goDir = 1;
		}
		else
		{
			goDir = 0;
		}

		dfs(x + dx[goDir], y + dy[goDir], goDir);
	}
}
vector<pair<int, int> > topsort;
bool used[2507][2];
int xid[2507], yid[2507];
void dfsTop(int x, int y)
{
	used[x][y] = true;
	for (int i = 0; i < (int)g[x][y].size(); i++)
	{
		int xx = g[x][y][i].fi, yy = g[x][y][i].se;
		if (!used[xx][yy])
		{
			dfsTop(xx, yy);
		}
	}
	topsort.push_back(make_pair(x, y));
}
int color[2507][2];
void dfsCol(int x, int y, int c)
{
	color[x][y] = c;
	for (int i = 0; i < (int)rg[x][y].size(); i++)
	{
		int xx = rg[x][y][i].fi, yy = rg[x][y][i].se;
		if (color[xx][yy] == 0)
		{
			dfsCol(xx, yy, c);
		}
	}
}
int zhfs()
{
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++)
		{
			scanf("%s", a[i]);
			for (int j = m; j >= 1; j--)
			{
				a[i][j] = a[i][j - 1];
				can[i][j].clear();
			}
		}
		int nextId = 1;
		bool FAIL = false;
		for (int i = 1; i <= n * m; i++)
		{
			g[i][0].clear();
			rg[i][0].clear();
			g[i][1].clear();
			rg[i][1].clear();
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] == '-' || a[i][j] == '|')
				{
					pts.clear();
					memset(was, 0, sizeof(was));
					id[i][j] = nextId;
					xid[nextId] = i;
					yid[nextId] = j;
					nextId++;
					dfs(i, j - 1, 3);
					dfs(i, j + 1, 1);
					ok[i][j][0] = ok[i][j][1] = true;
					for (int k = 0; k < (int)pts.size(); k++)
					{
						int x = pts[k].fi, y = pts[k].se;
						if (a[x][y] == '|' || a[x][y] == '-') ok[i][j][0] = false;
					}
					if (ok[i][j][0])
					{
						for (int k = 0; k < (int)pts.size(); k++)
						{
							int x = pts[k].fi, y = pts[k].se;
							if (a[x][y] == '.')
							{
								can[x][y].push_back(make_pair(id[i][j], 0));
							}
						}
					}
					if (!ok[i][j][0])
					{
						addEdge(mp(id[i][j], 0), mp(id[i][j], 1));
					}
					pts.clear();
					memset(was, 0, sizeof(was));
					dfs(i - 1, j, 2);
					dfs(i + 1, j, 0);
					for (int k = 0; k < (int)pts.size(); k++)
					{
						int x = pts[k].fi, y = pts[k].se;
						if (a[x][y] == '|' || a[x][y] == '-') ok[i][j][1] = false;
					}
					if (ok[i][j][1])
					{
						for (int k = 0; k < (int)pts.size(); k++)
						{
							int x = pts[k].fi, y = pts[k].se;
							if (a[x][y] == '.')
							{
								can[x][y].push_back(make_pair(id[i][j], 1));
							}
						}
					}
					if (!ok[i][j][1])
					{
						addEdge(mp(id[i][j], 1), mp(id[i][j], 0));
					}
					if (!ok[i][j][0] && !ok[i][j][1]) FAIL = true;
				}
			}
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] == '.' && can[i][j].empty())
				{
					FAIL = true;
				}
			}
		}
		if (FAIL)
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		nextId--;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] != '.') continue;
				if ((int)can[i][j].size() == 2)
				{
					addEdge(mp(can[i][j][0].fi, can[i][j][0].se ^ 1), can[i][j][1]);
					addEdge(mp(can[i][j][1].fi, can[i][j][1].se ^ 1), can[i][j][0]);
				}
				else
				{
					addEdge(mp(can[i][j][0].fi, can[i][j][0].se ^ 1), can[i][j][0]);
				
				}
			}
		}
		topsort.clear();
		memset(used, 0, sizeof(used));
		for (int i = 1; i <= nextId; i++)
		{
			for (int j = 0; j < 2; j++)
			{
				if (!used[i][j]) dfsTop(i, j);
			}
		}
		reverse(topsort.begin(), topsort.end());
		memset(color, 0, sizeof(color));
		for (int i = 0; i < (int)topsort.size(); i++)
		{
			int x = topsort[i].fi, y = topsort[i].se;
			if (color[x][y] == 0)
			{
				dfsCol(x, y, i + 1);
			}
		}
		for (int i = 1; i <= nextId; i++)
		{
			if (color[i][0] == color[i][1])
			{
				FAIL = true;
			}
		}
		if (FAIL)
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		for (int i = 1; i <= nextId; i++)
		{
			if (color[i][0] > color[i][1])
			{
				a[xid[i]][yid[i]] = '-';
			}
			else
			{
				a[xid[i]][yid[i]] = '|';
			}
		}
		printf("Case #%d: POSSIBLE\n", tt);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				printf("%c", a[i][j]);
			}
			printf("\n");
		}
		cerr << tt << endl;
	}
}

