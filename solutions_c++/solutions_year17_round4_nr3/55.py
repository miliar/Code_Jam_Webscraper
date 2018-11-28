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
struct edge { int src, dst; };

int const MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-12;
int INF = INT_MAX / 10;

#define VAR(x) ((x) << 1)
#define NOT(x) ((x) ^ 1)
typedef vector<vector<edge> > graph;
void visit(int v, const graph &g,
    vector<int> &ord, vector<int> &num, int k) {
  if (num[v] >= 0) return;
  num[v] = k;
  for (int i = 0; i < g[v].size(); ++i)
    visit(g[v][i].dst, g, ord, num, k);
  ord.push_back(v);
}
typedef pair<int,int> clause;
bool two_satisfiability(int m, const vector<clause> &cs) {
  int n = m * 2; // m positive vars and m negative vars
  graph g(n), h(n);
  for (int i = 0; i < cs.size(); ++i) {
    int u = cs[i].first, v = cs[i].second;
	g[NOT(u)].push_back( edge{NOT(u), v} );
	g[NOT(v)].push_back( edge{NOT(v), u} );
	h[v].push_back( edge{v, NOT(u)} );
	h[u].push_back( edge{u, NOT(v)} );
  }
  vector<int> num(n, -1), ord, dro;
  for (int i = 0; i < n; ++i)
    visit(i, g, ord, num, i);
  reverse(ord.begin(), ord.end());
  fill(num.begin(), num.end(), -1);
  for (int i = 0; i < n; ++i)
    visit(ord[i], h, dro, num, i);
  for (int i = 0; i < n; ++i)
    if (num[i] == num[NOT(i)])
      return false;
  return true;
}

int dy[] = {0, -1, 0, 1};
int dx[] = {-1, 0, 1, 0};

int H, W;
char a[100][100];
vector<int> b[100][100];

bool f(int i, int y, int x, int k) {
	y += dy[k]; x += dx[k];
	if (!(0<=y && y<H && 0<=x && x<W)) return false;
	if (a[y][x] == '#') return false;
	if (a[y][x] == '-') return true;
	if (a[y][x] == '/') k = vector<int>{3, 2, 1, 0}[k];
	if (a[y][x] == '\\') k = vector<int>{1, 0, 3, 2}[k];
	bool z = f(i, y, x, k);
	if (!z && a[y][x] == '.') b[y][x].pb(i);
	return z;
}

int main() {
	int T; cin >> T;
	rep(t, T) {
		cin >> H >> W;
		rep(y, H) rep(x, W) b[y][x].clear();
		rep(y, H) scanf("%s", a[y]);
		rep(y, H) rep(x, W) if (a[y][x] == '|') a[y][x] = '-';
		int N = 0;
		vector<vector<int> > c(H, vector<int>(W, -1));
		rep(y, H) rep(x, W) if (a[y][x] == '-') c[y][x] = N++;
		vector<bool> yoko(N, true), tate(N, true);
		rep(y, H) rep(x, W) if (a[y][x] == '-') {
			int i = c[y][x];
			if (f(i, y, x, 0)) yoko[i] = false;
			if (f(i, y, x, 2)) yoko[i] = false;
			if (f(N + i, y, x, 1)) tate[i] = false;
			if (f(N + i, y, x, 3)) tate[i] = false;
		}
		bool ok = true;
		vector<i_i> ps;
		rep(y, H) rep(x, W) if (a[y][x] == '.') {
			vector<int>& v = b[y][x];
			if (v.empty()) ok = false;
			if (v.size() == 1) {
				int i = v[0];
				if (i < N) tate[i] = false;
				else yoko[i - N] = false;
			}
			if (v.size() == 2) ps.pb(i_i(v[0], v[1]));
			if (v.size() >= 3) {
				cout << "ERR" << endl;
				return 0;
			}
		}
		if (!ok) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
			continue;
		}
		vector<clause> G;
		rep(i, N) {
			if (!yoko[i]) G.pb(i_i(NOT(VAR(i)), NOT(VAR(i))));
			if (!tate[i]) G.pb(i_i(VAR(i), VAR(i)));
		}
		for (i_i p: ps) {
			int x = (p.first < N ? VAR(p.first) : NOT(VAR(p.first - N)));
			int y = (p.second < N ? VAR(p.second) : NOT(VAR(p.second - N)));
			G.pb(i_i(x, y));
		}
		if (!two_satisfiability(N, G)) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
			continue;
		}
		printf("Case #%d: POSSIBLE\n", t + 1);
		vector<bool> ans(N);
		rep(i, N) {
			G.pb(i_i(VAR(i), VAR(i)));
			ans[i] = true;
			if (two_satisfiability(N, G)) continue;
			G.pop_back();
			G.pb(i_i(NOT(VAR(i)), NOT(VAR(i))));
			ans[i] = false;
		}
		rep(y, H) rep(x, W) if (a[y][x] == '-') {
			int i = c[y][x];
			a[y][x] = (ans[i] ? '-' : '|');
		}
		rep(y, H) printf("%s\n", a[y]);
	}
}
