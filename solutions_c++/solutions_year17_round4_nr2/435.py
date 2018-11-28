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
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr(T x) { return x * x; }

const int NMAX = 101;

int n, m, k;
int dn[1050], dm[1050];
int a[1050][1050];

int calc(int ans) {
	int p = 0;
	int h = 0;
	for (int i = m - 1; i >= 0; i--) {
		if (dm[i] > ans) {
			p += dm[i] - ans;
			h += dm[i] - ans;
		} else {
			int x = min(h, ans - dm[i]);
			h -= x;
		}
	}
	if (h > 0) return -1;
	return p;
}

void solve() {
	seta(a, 0);
	seta(dn, 0);
	seta(dm, 0);
	cin >> m >> n >> k;
	forn(i, k) {
		int xn, xm;
		cin >> xm >> xn;
		xn--;
		xm--;
		dn[xn]++;
		dm[xm]++;
		a[xn][xm]++;
	}
	int l = 1;
	forn(i, n) l = max(l, dn[i]);
	int r = k;
	while (l < r) {
		int mid = (l + r) / 2;
		if (calc(mid) == -1)
			l = mid + 1;
		else
			r = mid;
	}
	cout << l << " " << calc(l) << endl;
}

int main() {
	//	freopen ((task + ".in").data(), "r", stdin);
	//	freopen ((task + ".out").data(), "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.in.out.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
