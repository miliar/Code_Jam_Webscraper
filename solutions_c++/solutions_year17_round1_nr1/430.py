#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
#include <random>
#include <unordered_set>
#include <complex>
using namespace std;

#define rep(i, N) for (int i = 0; i < N; i++)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };
// typedef complex<double> C;

const int MOD = 1e9 + 7;
const int _MOD = 1000000009;
const int INF = INT_MAX / 2;
double EPS = 1e-10;

void solve() {
	int H, W; cin >> H >> W;
	vector<string> a(H);
	rep(y, H) cin >> a[y];
	rep(y, H) {
		char c = '?';
		rep(x, W) if (a[y][x] != '?') {
			c = a[y][x];
			break;
		}
		rep(x, W) {
			if (a[y][x] != '?') c = a[y][x];
			a[y][x] = c;
		}
	}
	rep(x, W) {
		char c = '?';
		rep(y, H) if (a[y][x] != '?') {
			c = a[y][x];
			break;
		}
		rep(y, H) {
			if (a[y][x] != '?') c = a[y][x];
			a[y][x] = c;
		}
	}
	rep(y, H) cout << a[y] << endl;
}

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		solve();
	}
}
