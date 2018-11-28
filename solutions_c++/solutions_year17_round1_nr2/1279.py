#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;


int d[55][55][2];
int r[55];
int q[55][55];
int nxt[55];

int h[1010];
int m;

const double EPS = 1e-6;


int main() {
  freopen("/Users/yogy/ClionProjects/untitled/B-small-attempt0.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/B.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    int n, p;
    scanf("%d%d", &n, &p);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &r[i]);
    }
    m = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        scanf("%d", &q[i][j]);
      }
      sort(q[i], q[i] + p);
      for (int j = 0; j < p; ++j) {
        d[i][j][0] = ceil ((q[i][j]) / (1.1 * r[i]));
        d[i][j][1] = floor ((q[i][j]) / (0.9 * r[i]));
//        printf("%d %d\n", d[i][j][0], d[i][j][1]);
        if (d[i][j][1] == 0) continue;
        if (d[i][j][0] == 0) d[i][j][0] = 1;
        h[m++] = d[i][j][0];
      }
    }
    sort(h, h + m);

//    for (int i = 0; i < m; ++i) {
//      printf("h[%d]=%d\n",i,h[i]);
//    }

    memset(nxt, 0, sizeof(nxt));
    int ans = 0;
    for (int hi = 0; hi < m; ++hi) {
      if (!h[hi]) continue;
      bool finish = false;
      int t = h[hi];
      for (int i = 0; i < n; ++i) {
        while (nxt[i] < p && d[i][nxt[i]][1] < t) {
          ++nxt[i];
        }
        if (nxt[i] == p) {
          finish = true;
          break;
        }
        if (d[i][nxt[i]][0] > t) {
          goto L;
        }
      }
      if (!finish) {
        ++ans;
        for (int i = 0; i < n; ++i) {
          ++nxt[i];
        }
      }

      for (int i = 0; i < n; ++i) {
        if (nxt[i] == p) {
          finish = true;
          break;
        }
      }
      if (finish) break;
      L:;
    }

    printf("Case #%d: %d\n", ++tc, ans);

  }
  return 0;
}