#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <bitset>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define next NEXT64
#define prev PREV64
#define y1 Y164

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 29) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr(T x) { return x * x; }

int n, q;
int64 e[500], s[500];
int64 d[500][500];
double ans[500][500];

void solve() {
	cin >> n >> q;
	forn(i, n) {
		cin >> e[i] >> s[i];
	}
	seta(ans, 0);
	seta(d, 0);
	forn(i, n)
		forn(j, n) {
			int x;
			scanf("%d", &x);
			d[i][j] = x;
			if (d[i][j] == -1) d[i][j] = inf64;
	}
	forn(i, n) d[i][i] = 0;
	forn(k, n)
		forn(i, n)
			forn(j, n)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	forn(i, n) {
		forn(j, n) {
			if (d[i][j] <= e[i])
				ans[i][j] = (double)d[i][j] / (double)s[i];
			else
				ans[i][j] = (double)inf64;
		}
	}

	forn(k, n)
		forn(i, n)
			forn(j, n)
				ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j]);
	forn(i, q) {
		int x, y;
		scanf("%d%d", &x, &y);
		x--;
		y--;
		printf(" %.6lf", ans[x][y]);
	}
	printf("\n");
}

int main() {
	//	freopen ((task + ".in").data(), "r", stdin);
	//	freopen ((task + ".out").data(), "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.in.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; i++) {
		printf("Case #%d:", i);
		solve();
	}
	return 0;
}
