#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

bool b[1440][2];
int d[1440][721][2][2];

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/B-large.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/B-large.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    memset(d, 0x3f, sizeof(d));
    memset(b, 0, sizeof(b));
    int ans = 1440, n[2], s, e;
    scanf("%d%d", &n[0], &n[1]);
    for (int t = 0; t < 2; ++t) {
      for (int i = 0; i < n[t]; ++i) {
        scanf("%d%d", &s, &e);
        for (int j = s; j < e; ++j) {
          b[j][t] = 1;
        }
      }
    }
    for (int t = 0; t < 2; ++t) {
      if (b[0][t]) continue;
      d[0][1][t][t] = 0;
      for (int i = 1; i < 1440; ++i) {
        for (int j = 0; j < 2; ++j) {
          if (b[i][j]) continue;
          for (int k = 1; k <= min(i + 1, 720); ++k) {
            d[i][k][j][t] = min(d[i - 1][k - 1][j][t], d[i - 1][i - k + 1][1 - j][t] + 1);
//            if(i==180 && d[i][k][j][t] <= 1440) printf("d[%d][%d][%d][%d]=%d\n", i, k, j, t, d[i][k][j][t]);
          }
        }
      }
      ans = min(ans, d[1439][720][t][t]);
      ans = min(ans, d[1439][720][1 - t][t] + 1);
    }
    printf("Case #%d: %d\n", ++tc, ans);
  }
  return 0;
}