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
#include <unordered_map>
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

int const MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-12;
int INF = INT_MAX / 10;

i_i solve() {
	int N, C, M; cin >> N >> C >> M;
	vector<int> p(M), b(M);
	rep(j, M) cin >> p[j] >> b[j], p[j]--, b[j]--;
	vector<int> num(C);
	rep(j, M) num[b[j]]++;
	int ma = 0;
	rep(c, C) ma = max(ma, num[c]);
	vector<int> unko(N);
	rep(j, M) unko[p[j]]++;
	for (int d = ma; ; d++) {
		bool ok = true;
		int sum = 0;
		rep(i, N) {
			sum += unko[i];
			if (sum > (i + 1) * d) ok = false;
		}
		if (ok) {
			int ans = 0;
			rep(i, N) ans += max(0, unko[i] - d);
			return i_i(d, ans);
		}
	}
}

int main() {
	int T; cin >> T;
	rep(t, T) {
		i_i p = solve();
		printf("Case #%d: %d %d\n", t + 1, p.first, p.second);
	}
}
