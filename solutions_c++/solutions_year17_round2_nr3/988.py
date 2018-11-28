#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

const int MaxN = 100;
const LL infDist = 1000LL * 1000LL * 1000LL * 1000LL * 100LL;  // 10^14
const dbl infTime = 1000LL * 1000LL * 1000LL * 1000LL; // 10^12
LL g[MaxN + 10][MaxN + 10];
LL d[MaxN + 10][MaxN + 10];
LL e[MaxN + 10];
LL s[MaxN + 10];
dbl tm[MaxN + 10][MaxN + 10]; // tm[horse][city] = minTime

void calcTime(int n)
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			d[i][j] = g[i][j] == -1 ? infDist : g[i][j];

	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			d[i][j] = min(d[i][j], infDist);

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			if (d[i][j] <= e[i])
				tm[i][j] = ((dbl)d[i][j]) / ((dbl)(s[i]));
			else
				tm[i][j] = infTime;
		tm[i][i] = 0;
	}

	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				tm[i][j] = min(tm[i][j], tm[i][k] + tm[k][j]);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			tm[i][j] = min(tm[i][j], infTime);
}

void solve()
{
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++)
		cin >> e[i] >> s[i];

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> g[i][j];

	calcTime(n);
	for (int Q = 0; Q < q; Q++)
	{
		int u, v;
		cin >> u >> v;
		cout << " " << tm[u][v];
	}

	cout << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("C-large.in", "r", stdin);
	freopen("output_C_large.txt","w",stdout);
	cout << fixed;
	cout << setprecision(9);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ":";
		solve();
	}

	return 0;
}