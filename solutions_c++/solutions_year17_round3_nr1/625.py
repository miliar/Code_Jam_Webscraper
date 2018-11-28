#include <bits/stdc++.h>
using namespace std;

const double PI = acos(-1.0);

typedef pair<double, double> pdd;
double f[1111][1111];
pdd a[1111];


int main(void) {

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);
    int N, K; scanf("%d %d", &N, &K);
    for (int i = 1; i <= N; ++i) {
      scanf("%lf %lf", &a[i].first, &a[i].second);
    }
    sort(a + 1, a + N + 1);
    reverse(a + 1, a + N + 1);
    memset(f, 0, sizeof f);
    for (int i = 1; i <= K; ++i)
      for (int j = 1; j <= N; ++j) {
        f[i][j] = max(f[i][j], f[i][j-1]);
        double extra = PI * 2.0 * a[j].first * a[j].second;
        if (i == 1) {
          extra += PI * a[j].first * a[j].first;
        }
        f[i][j] = max(f[i][j], f[i-1][j-1] + extra);
      }
    printf("%.10f\n", f[K][N]);
  }


  return 0;
}