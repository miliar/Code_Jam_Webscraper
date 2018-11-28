// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;
#define int long long
#define double long double
const int N = (int) 105, mod = (int) 0;
double d[N][N];
long long travel[N], speed[N], dd[N][N];
int32_t main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		int n, q;
		cin >> n >> q;
		for (int j = 0; j < n; ++j) {
			cin >> travel[j] >> speed[j];
		}
		for (int a = 0; a < n; ++a) {
			for (int b = 0; b < n; ++b) {
				cin >> dd[a][b];
				if (dd[a][b] == -1) {
					dd[a][b] = 1e18;
				}
			}
		}
		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					dd[i][j] = min(dd[i][k] + dd[k][j], dd[i][j]);
		for (int v = 0; v < n; ++v) {
			for (int j = 0; j < n; ++j) {
				if (dd[v][j] > travel[v]) {
					d[v][j] = 1e18;
				} else {
					d[v][j] = (double) dd[v][j] / speed[v];
				}
			}
		}
		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		cout << setprecision(8) << fixed;
		while (q--) {
			int u, v;
			cin >> u >> v;
			--u, --v;
			cout << d[u][v] << ' ';
		}
		cout << endl;
	}
}

















