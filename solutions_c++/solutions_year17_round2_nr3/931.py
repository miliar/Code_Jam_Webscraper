#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

LL min(LL x, LL y) { return x < y ? x : y; }

LL N, Q;
LL E[200], S[200];
LL a[200][200];
double c[200][200];

int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", ++cas);
    scanf("%lld%lld", &N, &Q);
    for (int i = 0; i < N; ++i) {
      scanf("%lld%lld", &E[i], &S[i]);
    }
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        scanf("%lld", &a[i][j]);
        if (a[i][j] == -1) a[i][j] = 1ll << 50;
        c[i][j] = 1e20;
        if (i == j) c[i][j] = 0;
      }
    }
    for (int k = 0; k < N; ++k) {
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
          a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
        }
      }
    }
    /*
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        printf("%lld ", a[i][j]);
      }
    } puts("");
    */
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (a[i][j] <= E[i]) {
          c[i][j] = (a[i][j] * 1.0) / S[i];
        }
      }
    }
    for (int k = 0; k < N; ++k) {
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
          if (c[i][k] + c[k][j] + 1e-9 < c[i][j]) {
            c[i][j] = c[i][k] + c[k][j];
          }
          //c[i][j] = min(c[i][j], c[i][k] + c[k][j]);
        }
      }
    }
    while (Q--) {
      int s, t;
      scanf("%d%d", &s, &t);
      --s; --t;
      if (Q) {
        printf("%6f ", c[s][t]);
      } else {
        printf("%6f\n", c[s][t]);
      }
    }
  }
  return 0;
}
