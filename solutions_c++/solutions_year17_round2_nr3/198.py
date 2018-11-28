#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<double, int> state;

const int MAXN = 110;
const ll INF = 1LL << 40;

int n, q;
int hl[MAXN], hs[MAXN];
ll d[MAXN][MAXN];

double query(int u, int v) {
  static double dist[MAXN];
  static priority_queue<state, vector<state>, greater<state>> pq;
  REP(i, n) dist[i] = 1e15;
  dist[u] = 0;
  pq.push({0, u});
  while (!pq.empty()) {
    state s = pq.top(); pq.pop();
    int x = s.second;
    if (dist[x] < s.first)
      continue;
    REP(y, n) {
      if (d[x][y] > hl[x]) continue;
      double tm = (double)d[x][y] / hs[x];
      if (dist[x] + tm < dist[y]) {
        dist[y] = dist[x] + tm;
        pq.push({dist[y], y});
      }
    }
  }
  return dist[v];
}

void solve() {
  scanf("%d%d", &n, &q);
  REP(i, n) scanf("%d%d", &hl[i], &hs[i]);
  REP(i, n) REP(j, n) scanf("%lld", &d[i][j]);
  REP(i, n) REP(j, n) if (d[i][j] == -1) d[i][j] = INF;
  REP(i, n) d[i][i] = 0;
  REP(k, n) REP(i, n) REP(j, n) {
    if (k == i || j == i || k == j) continue;
    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
  }
  REP(i, q) {
    int u, v;
    scanf("%d%d", &u, &v);
    --u; --v;
    printf("%.8lf%c", query(u, v), " \n"[i == q-1]);
  }  
}

int main(void) {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    solve();
  }
  return 0;
}

