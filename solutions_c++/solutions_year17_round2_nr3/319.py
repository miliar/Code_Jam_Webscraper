#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <ctime>
#include <hash_map>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef pair<int, int> pii;
typedef long long int64;
typedef pair<int64, int64> pii64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;
typedef pair<int64,pii> piii64;
typedef pair<pii,pii> piiii;
typedef pair<double, double> pdd;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa
#define y0 _sdkfsjfs__
#define tm _dskfjskdfjksdf

int nt;
int n, q;
vector<int> e;
vector<int> s;
vector< vector<int64> > a;

inline void init()
{
	scanf("%d%d", &n, &q);
	e.resize(n);
	s.resize(n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d", &e[i], &s[i]);
	}
	a.resize(n);
	int x = 0;
	for (int i = 0; i < n; ++i)
	{
		a[i].resize(n);
		for (int j = 0; j < n; ++j)
		{
			scanf("%d", &x);
			a[i][j] = x;
		}
	}
	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				if (a[i][k] == -1 || a[k][j] == -1) continue;
				if (a[i][j] == -1 || a[i][j] > a[i][k] + a[k][j])
				{
					a[i][j] = a[i][k] + a[k][j];
				}
			}
}

vector<double> l;
vector<bool> was;

inline double dijkstra(int u, int v)
{
	const double maxval = 1e+21;
	const double lim = 1e+20;
	l.clear();
	was.clear();
	l.assign(n, maxval);
	was.assign(n, false);
	l[u] = 0;
	int x = u;
	while (x != -1)
	{
		was[x] = true;
		double vel = s[x];
		for (int j = 0; j < n; ++j)
		{
			if (a[x][j] == -1) continue;
			if (a[x][j] > e[x]) continue;
			double t = a[x][j] / vel;
			l[j] = min(l[j], l[x] + t);
		}
		x = -1;
		for (int i = 0; i < n; ++i)
		{
			if (was[i]) continue;
			if (l[i] > lim) continue;
			if (x == -1)
				x = i;
			if (l[x] > l[i])
				x = i;
		}
		if (x == v) break;
	}
	return l[v];
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		printf("Case #%d:", tn);
		int u = 0, v = 0;
		for (int t = 0; t < q; ++t)
		{
			scanf("%d%d", &u, &v);
			--u, --v;
			double res = dijkstra(u, v);
			printf(" %.15lf", res);
		}
		printf("\n");
	}

	return 0;
}