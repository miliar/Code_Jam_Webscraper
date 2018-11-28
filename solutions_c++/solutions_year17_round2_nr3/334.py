#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 110;
const llint inf = 1e18;

int E[MAX], S[MAX];
llint d[MAX][MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, Q;
    scanf("%d %d", &N, &Q);
    REP(i, N) scanf("%d %d", &E[i], &S[i]);
    REP(i, N) REP(j, N) {
      scanf("%lld", &d[i][j]);
      if (d[i][j] == -1) d[i][j] = inf;
    }

    REP(k, N) REP(i, N) REP(j, N) {
      d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }

    printf("Case #%d:", tp);
    REP(i, Q) {
      int u, v;
      scanf("%d %d", &u, &v);
      --u, --v;

      vector<double> f(N, inf);
      vector<bool> bio(N, false);
      f[u] = 0;

      while (true) {
        int x = -1;
        REP(j, N) {
          if (f[j] < inf && !bio[j]) {
            if (x == -1 || f[j] < f[x]) {
              x = j;
            }
          }
        }
        if (x == -1) break;

        bio[x] = true;
        REP(y, N) {
          if (d[x][y] <= E[x]) {
            f[y] = min(f[y], f[x] + d[x][y] * 1.0 / S[x]);
          }
        }
      }

      printf(" %.10lf", f[v]);
    }
    printf("\n");
  }
  return 0;
}
