#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

// #ifdef DEBUG
// #define dbg(fmt, args...) fprintf(stderr, fmt, ##args)
// #else
#define dbg(fmt, args...)
// #endif
#define REPS(i, s, n) for(int (i) = (s); (i) < (int)(n); ++(i))
#define REPRS(i, e, n) for(int (i) = (int)(n) - 1; (i) >= e; --(i))
#define REPR(i, n) REPRS(i, 0, n)
#define REP(i, n) REPS(i, 0, n)
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mp make_pair
#define x first
#define y second
#define INFI 1234567890
#define INFL 1234567890123456789LL
typedef double dbl;
typedef long double ldbl;
typedef long long ll;

using namespace std;

int n, q;
vector<vector<ll>> g;
vector<vector<ll>> d;
vector<vector<ldbl>> gt;
vector<ll> e, s;

ldbl sub_solve(int u, int v) {
  return gt[u][v];
}

vector<ldbl> solve() {
  scanf("%d%d", &n, &q);
  e.clear();
  e.resize(n);
  s.clear();
  s.resize(n);
  dbg("OK1 n = %d, q = %d\n", n, q);
  REP(i, n) {
    scanf("%lld%lld", &e[i], &s[i]);
  }
  g.clear();
  g.resize(n, vector<ll>(n, 0));
  gt.clear();
  gt.resize(n, vector<ldbl>(n, 0));
  REP(i, n) {
    REP(j, n) {
      scanf("%lld", &g[i][j]);
      if (g[i][j] < 0) g[i][j] = INFL;
    }
  }
  d = g;
  REP(k, n) {
    REP(i, n) {
      REP(j, n) {
        if (d[i][k] < INFL && d[k][j] < INFL) {
          d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
      }
    }
  }
  vector<ldbl> answer;
  REP(i, n) {
    REP(j, n) {
      if (d[i][j] <= e[i]) {
        gt[i][j] = (ldbl)d[i][j] / s[i];
      } else {
        gt[i][j] = INFL;
      }
    }
  }
  REP(k, n) {
    REP(i, n) {
      REP(j, n) {
        if (gt[i][k] + (ldbl)10 < INFL && gt[k][j] + (ldbl)10 < INFL) {
          gt[i][j] = min(gt[i][j], gt[i][k] + gt[k][j]);
        }
      }
    }
  }
  REP(i, q) {
    int u, v;
    scanf("%d%d", &u, &v);
    --u, --v;
    dbg("OK10 u = %d, v = %d\n", u, v);
    answer.pb(sub_solve(u, v));
  }
  return answer;
}


int main() {
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    dbg("Case #%d\n", test);
    fprintf(stderr, "Case #%d\n", test);
    vector<ldbl> answer = solve();
    printf("Case #%d: ", test);
    REP(i, answer.size()) {
      printf("%.08lf%c", (dbl)answer[i], " \n"[i + 1 == answer.size()]);
    }
  }
  return 0;
}
