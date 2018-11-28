#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#define INF 100000
#define min(a, b) ((a) < (b) ? (a) : (b))
using namespace std;

int f[1500][1000], g[1500][1000];
int t[1500];

int main () {
  int T;
  cin >> T;

  for (int _ = 1; _ <= T; ++_) {
    cout << "Case #" << _ << ": ";

    int c, j, l, r;
    cin >> c >> j;

    for (int i = 0; i < 1440; ++i) { t[i] = 0; }
    for (int i = 0; i < c; ++i) {
      cin >> l >> r;
      for (int k = l; k < r; ++k) t[k] = 1;
    }
    for (int i = 0; i < j; ++i) {
      cin >> l >> r;
      for (int k = l; k < r; ++k) t[k] = 2;
    }

    for (int i = 0; i < 1440; ++i) {
      for (int p = 0; p <= 720; ++p) f[i][p] = g[i][p] = INF;
      for (int p = 0; p <= i + 1 && p <= 720; ++p) {
        if (t[i] == 0) {
          if (i == 0) {
            if (p == 1) { f[i][p] = 0; g[i][p] = INF; }
            else if (p == 0) { f[i][p] = INF; g[i][p] = 0; }
            else { f[i][p] = g[i][p] = INF; }
          } else {
            if (p == 0) {
              f[i][p] = INF;
              g[i][p] = g[i - 1][p];
            } else {
              f[i][p] = min(f[i - 1][p - 1], g[i - 1][p - 1] + 1);
              g[i][p] = min(g[i - 1][p], f[i - 1][p] + 1);
            }
          }
        } else if (t[i] == 1) {
          g[i][p] = INF;
          if (i == 0) {
            if (p == 0) {
              f[i][p] = INF;
            } else {
              if (p == 1) {
                f[i][p] = 0;
              } else {
                f[i][p] = INF;
              }
            }
          } else {
            if (p == 0) {
              f[i][p] = INF;
            } else {
              f[i][p] = min(f[i - 1][p - 1], g[i - 1][p - 1] + 1);
            }
          }
        } else if (t[i] == 2) {
          f[i][p] = INF;
          if (i == 0) {
            if (p == 0) {
              g[i][p] = 0;
            } else {
              if (p == 1) {
                g[i][p] = INF;
              } else {
                g[i][p] = INF;
              }
            }
          } else {
            if (p == 0) {
              g[i][p] = g[i - 1][p];
            } else {
              g[i][p] = min(g[i - 1][p], f[i - 1][p] + 1);
            }
          }
        }
      }
    }

    int ans = min(f[1439][720], g[1439][720]);
    if (ans % 2) ans++;

    cout << ans << endl;
  }

  return 0;
}
