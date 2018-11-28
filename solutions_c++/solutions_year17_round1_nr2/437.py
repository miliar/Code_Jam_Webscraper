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

int solve() {
	int N, M; cin >> N >> M;
	vector<int> a(N);
	rep(i, N) cin >> a[i];
	vector<vector<int> > b(N, vector<int>(M));
	rep(i, N) rep(j, M) cin >> b[i][j];
	rep(i, N) sort(b[i].begin(), b[i].end());
	vector<int> c(N);
	int ans = 0;
	for (int x = 1; x <= 1200000;) {
		bool ok = true;
		rep(i, N) {
			int &j = c[i];
			for (; j < M && b[i][j] * 10 < (ll)a[i] * x * 9; j++);
			if (j < M && b[i][j] * 10 <= (ll)a[i] * x * 11);
			else ok = false;
		}
		if (ok) {
			ans++;
			rep(i, N) c[i]++;
		}
		else x++;
	}
	return ans;
}

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: %d\n", t, solve());
		cerr << t << endl;
	}
}
