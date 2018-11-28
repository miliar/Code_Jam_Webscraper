#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

const int oneDay = 1440;
const int halfDay = 720;
const int MAXANS = 1e6;

int flag[oneDay + 10];
int f[oneDay + 10][halfDay + 10][2][2];
int T, n, m;

int main() {
  freopen("Blarge.in", "r", stdin);
  freopen("Blarge.out", "w", stdout);
  int T, n, m;
  int res, x, y, l0;
  scanf("%d", &T);
  rep(cas, 1, T + 1) {
    memset(flag, 0, sizeof(flag));
    scanf("%d%d", &n, &m);
    if (n + m == 0) {
      printf("Case #%d: 2\n", cas);
      continue;
    }
    rep(i, 0, n) {
      scanf("%d%d", &x, &y);
      rep(j, x, y)
        flag[j] = -1;
    }
    rep(i, 0, m) {
      scanf("%d%d", &x, &y);
      rep(j, x, y)
        flag[j] = 1;
    }
    rep(i, 0, oneDay + 10)
      rep(j, 0, halfDay + 10)
        rep(k, 0, 2)
          rep(l, 0, 2)
          f[i][j][k][l] = MAXANS;
    f[0][1][1][1] = 0;
    f[0][0][0][0] = 0;
    if (flag[0] == 1)
      f[0][1][1][1] = MAXANS;
    if (flag[0] == -1)
      f[0][0][0][0] = MAXANS;
    rep(i, 0, oneDay + 1)
      rep(j, 0, halfDay + 1)
//    rep(i, 0, 10)
//      rep(j, 0, 10)
        rep(k, 0, 2)
          rep(l, 0, 2) {
//            cout << i << " " << j << " " << k << " " << l << endl;
//            cout << flag[i] << " " << f[i][j][k][l] << endl;
            if (f[i][j][k][l] == MAXANS)
              continue;
            if (flag[i] == 1 && l == 1) {
              f[i][j][k][l] = MAXANS;
              continue;
            }
            if (flag[i] == -1 && l == 0) {
              f[i][j][k][l] = MAXANS;
              continue;
            }
            f[i + 1][j + l][k][l] = min(f[i + 1][j + l][k][l], f[i][j][k][l]);
            l0 = l ^ 1;
            f[i + 1][j + l0][k][l0] = min(f[i + 1][j + l0][k][l0], f[i][j][k][l] + 1);
          }
    res = MAXANS;
    rep(i, 0, 2)
      rep(j, 0, 2) {
        if (i == j)
          res = min(res, f[oneDay - 1][halfDay][i][j]);
        else
          res = min(res, f[oneDay - 1][halfDay][i][j] + 1);
      }
    printf("Case #%d: %d\n", cas, res);
  }
  return 0;
}
