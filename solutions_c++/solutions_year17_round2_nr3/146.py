#include <cstdio>
using namespace std;

const int maxN = 100 + 7;

double ans[maxN][maxN];
long long len[maxN][maxN];
int T, N, Q, t, u, v, e[maxN], s[maxN];

void updateLong(long long& u, long long v) { if (u < 0 || u > v) u = v; }
void updateDouble(double& u, double v) { if (u < 0 || u > v) u = v; }

void solve() {
  for (int k = 0; k < N; k ++)
    for (int i = 0; i < N; i ++)
      for (int j = 0; j < N; j ++)
        if (len[i][k] > 0 && len[k][j] > 0) updateLong(len[i][j], len[i][k] + len[k][j]);

  /* for (int i = 0; i < N; i ++) {
    for (int j = 0; j < N; j ++) printf("%lld ", len[i][j]);
    printf("\n");
  } */

  for (int i = 0; i < N; i ++)
    for (int j = 0; j < N; j ++) 
      if (len[i][j] > 0 && len[i][j] <= e[i]) ans[i][j] = (double)len[i][j] / s[i]; else ans[i][j] = -1;

  for (int k = 0; k < N; k ++)
    for (int i = 0; i < N; i ++)
      for (int j = 0; j < N; j ++)
        if (ans[i][k] > 0 && ans[k][j] > 0) updateDouble(ans[i][j], ans[i][k] + ans[k][j]);

  /* for (int i = 0; i < N; i ++) {
    for (int j = 0; j < N; j ++) printf("%lf ", ans[i][j]);
    printf("\n");
  } */
}

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%d%d", &N, &Q);
    for (int i = 0; i < N; i ++) scanf("%d%d", &e[i], &s[i]);
    for (int i = 0; i < N; i ++)
      for (int j = 0; j < N; j ++) scanf("%d", &t), len[i][j] = t;

    solve();

    printf("Case #%d:", cou);
    for (int i = 0; i < Q; i ++) {
      scanf("%d%d", &u, &v), u --, v --;
      printf(" %lf", ans[u][v]);
    }
    printf("\n");
  }
}
