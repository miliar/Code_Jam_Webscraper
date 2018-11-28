#include <vector>
#include <stack>
#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <functional>
#include <set>
#include <cstring>
#include <queue>
#include <stdlib.h>
#include <time.h>
#include <complex>
#include <iterator>
#include <regex>
#include <fstream>
#define all(o) (o).begin(), (o).end()
#define mp(x, y) make_pair(x, y)
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define sz(x) ((int)(x).size())
#define xx first
#define yy second
#define pt pair <double, double>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int S = int(1e3) + 10;
const int INF = int(1e9) + 7;
const ll MOD = ll(1e9) + 7;
const double EPS = 1e-12;
const ll magic = ll(5e4);
const int N = 1000;


int T, n, a[S], c, m, p[S], b[S];

int need(int m)
{
	int can = 0, must = 0;
	for(int i = 0; i < n; i++)
	{
		if(a[i] < m)
			can += (m - a[i]);
		if(a[i] > m)
			must += (a[i] - m);
		if(must > can)
			return -1;
	}
	return must;
}

int getmin()
{
	int l = 0, r = 1000;
	while(r - l > 1)
	{
		int m = (l + r)/2;
		if(need(m) == -1)
			l = m;
		else
			r = m;
	}
	return r;
}


int main()
{
	freopen("/Users/user/Downloads/B-large.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> T;
	for(int q = 1; q <= T; q++)
	{
		cin >> n >> c >> m;
		memset(a, 0, n*sizeof(int));
		for(int i = 0; i < m; i++)
		{
			scanf("%d%d", p + i, b + i);
			p[i]--;
			b[i]--;
		}
		int k = 0;
		for(int i = 0; i < c; i++)
		{
			int r = 0;
			for(int j = 0; j < m; j++)
				if(b[j] == i)
					r++;
			k = max(k, r);
		}
		for(int j = 0; j < m; j++)
			a[p[j]]++;
		int t = getmin();
		if(t <= k)
			printf("Case #%d: %d %d\n", q, k, need(k));
		else
			printf("Case #%d: %d %d\n", q, t, need(t));
//		printf("Case #%d: %d\n", q, res);
	}
	
	return 0;
}
