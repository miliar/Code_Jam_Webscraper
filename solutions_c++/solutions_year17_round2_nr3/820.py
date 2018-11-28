#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAXN = 100 + 10;

double DP[MAXN][MAXN];
double E[MAXN];
double S[MAXN];
double D[MAXN][MAXN];

int T, N, Q;
int main() {
  scanf("%d", &T);

  for (int t = 1;t <= T;++t) {
    scanf("%d %d", &N, &Q);
    for (int i = 0;i < N;++i) {
      scanf("%lf %lf", &E[i], &S[i]);
    }

    for (int i = 0;i < N;++i) {
      for (int j = 0;j < N;++j) {
        scanf("%lf", &D[i][j]);
      }
    }


    for (int i = N - 1;i >= 0;--i) {
      DP[i][i] = 0;
      for (int j = i + 1;j < N;++j) {
        DP[i][j] = -1;
        
        double d = 0;
        for (int k = i + 1;k <= j;++k) {
          d += D[k - 1][k];

          if (d > E[i] || DP[k][j] == -1) {
            continue;
          }

          if (DP[i][j] == -1)
            DP[i][j] = d / S[i] + DP[k][j];
          DP[i][j] = min(DP[i][j], d / S[i] + DP[k][j]);
        }
      }
    }
     
    int u, v;
    scanf("%d %d", &u, &v);
    u--;
    v--;
    printf("Case #%d: %lf\n", t, DP[u][v]);
  }
  return 0;
}
