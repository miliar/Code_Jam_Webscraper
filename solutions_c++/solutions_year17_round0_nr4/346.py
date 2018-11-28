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
#include <cassert>
using namespace std;

#define rep(i, N) for (int i = 0; i < N; i++)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<int, ll> i_ll;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
typedef vector<int> vi;

const int MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;
int INF = INT_MAX / 2;

struct edge { int v; ll c; int rev; };

struct flow_network {
	int n;
	vector< vector<edge> > G;
	flow_network(int _n) : n(_n), G(_n) {}
	void add_edge(int u, int v, ll c) {
		edge e = {v, c, G[v].size()}, _e = {u, 0, G[u].size()};
		G[u].push_back(e); G[v].push_back(_e);
	}
	ll dfs(int u, int t, ll f, vector<bool>& vis) {
		if (u == t) return f;
		vis[u] = true;
		for (int i = 0; i < G[u].size(); i++) {
			edge& e = G[u][i];
			if (vis[e.v] || e.c == 0) continue;
			ll d = min(e.c, dfs(e.v, t, min(f, e.c), vis));
			if (d == 0) continue;
			e.c -= d;
			G[e.v][e.rev].c += d;
			return d;
		}
		return 0;
	}
	ll max_flow(int s, int t) {
		ll res = 0;
		for (;;) {
			vector<bool> vis(n);
			ll f = dfs(s, t, LLONG_MAX, vis);
			if (f == 0) return res;
			res += f;
		}
	}
};

int main() {
	int T; cin >> T;
	rep(_t, T) {
		int N, M; cin >> N >> M;
		vector<vector<bool> > a(N, vector<bool>(N)), b = a, c = a;
		while (M--) {
			string s; int y, x;
			cin >> s >> y >> x;
			y--; x--;
			if (s == "x" || s == "o") a[y][x] = true;
			if (s == "+" || s == "o") b[y][x] = true;
		}
		rep(y0, N) rep(x0, N) {
			bool ok = true;
			rep(y, N) if (a[y][x0]) ok = false;
			rep(x, N) if (a[y0][x]) ok = false;
			if (ok) a[y0][x0] = c[y0][x0] = true;
		}
		vector<bool> pos1(N * 2 - 1, true), pos2 = pos1;
		rep(y, N) rep(x, N) if (b[y][x])
			pos1[y + x] = pos2[y - x + N - 1] = false;
		flow_network fn(N * 4);
		int s = N * 4 - 2, t = N * 4 - 1;
		rep(u, N * 2 - 1) if (pos1[u]) fn.add_edge(s, u, 1);
		rep(v, N * 2 - 1) if (pos2[v]) fn.add_edge(N * 2 - 1 + v, t, 1);
		rep(y, N) rep(x, N) {
			int u = y + x, v = y - x + N - 1;
			fn.add_edge(u, N * 2 - 1 + v, 1);
		}
		fn.max_flow(s, t);
		vector<vector<bool> > f(N * 4, vector<bool>(N * 4));
		rep(u, N * 2 - 1) for (edge e: fn.G[u]) if (!e.c) f[u][e.v] = true;
		rep(u, N * 2 - 1) rep(v, N * 2 - 1) {
			int df = f[u][N * 2 - 1 + v] - f[N * 2 - 1 + v][u];
			if (df == 1) {
				int y = (u + v - N + 1) / 2;
				int x = (u - v + N - 1) / 2;
				b[y][x] = c[y][x] = true;
			}
		}
		M = 0;
		rep(y, N) rep(x, N) if (c[y][x]) M++;
		int score = 0;
		rep(y, N) rep(x, N) score += a[y][x] + b[y][x];
		printf("Case #%d: %d %d\n", _t + 1, score, M);
		rep(y, N) rep(x, N) if (c[y][x])
			cout << ".x+o"[a[y][x] + b[y][x] * 2] << ' ' << y + 1 << ' ' << x + 1 << endl;
	}
}
