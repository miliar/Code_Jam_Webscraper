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
const int S = int(1e2) + 10;
const ll INF = ll(1e15) + 7;
const ll MOD = ll(1e9) + 7;
const double EPS = 1e-12;
const ll magic = ll(5e4);




ll e[S], s[S], d[S][S], qq;
int n, T;
double t[S][S];


int main()
{
	freopen("/Users/user/Downloads/C-large.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> T;
//	printf("Case #%d: IMPOSSIBLE\n", q);
	for(int q = 1; q <= T; q++)
	{
		cin >> n >> qq;
		for(int i = 0; i < n; i++)
			scanf("%lld%lld", e + i, s + i);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				scanf("%lld", &d[i][j]);
				if(d[i][j] == -1)
					d[i][j] = INF;
				if(i == j)
					d[i][j] = 0;
			}
		
		vector <pair <int, int>> qs;
		qs.resize(qq);
		for(int i = 0; i < qq; i++)
			scanf("%d%d", &qs[i].xx, &qs[i].yy);
		
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if(d[i][j] > e[i])
					t[i][j] = INF;
				else
					t[i][j] = double(d[i][j])/s[i];
		
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
		
		printf("Case #%d: ", q);
		for(int i = 0; i < qq; i++)
			printf("%lf ", t[qs[i].xx - 1][qs[i].yy - 1]);
		printf("\n");
	}
	return 0;
}
