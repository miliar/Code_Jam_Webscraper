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
const double INF = 1e15 + 7;
const ll MOD = ll(1e9) + 7;
const double EPS = 1e-12;
const ll magic = ll(5e4);




int n;
int T;
double d;


int main()
{
	freopen("/Users/user/Downloads/A-large.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> T;
	for(int q = 1; q <= T; q++)
	{
		
		double v = INF;
		cin >> d >> n;
		for(int i = 0; i < n; i++)
		{
			double s, k;
			scanf("%lf%lf", &k, &s);
			v = min(v, d*s/(d - k));
		}
		printf("Case #%d: %lf\n", q, v);
	}
	return 0;
}
