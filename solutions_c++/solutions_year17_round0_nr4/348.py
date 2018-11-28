#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

const int MAXN = 110;

int a[MAXN][MAXN], b[MAXN][MAXN];
int iA[MAXN][MAXN], iB[MAXN][MAXN];
bool ax[MAXN * 3], ay[MAXN * 3];
bool bx[MAXN * 3], by[MAXN * 3];
int n, m;

int main() {
  freopen("D.in", "r", stdin);
  freopen("D.out", "w", stdout);
  int T, x, y, resx, resy;
  int x1, y1, x2, y2;
  char c;
  cin >> T;
  rep(t, 1, T + 1) {
    cin >> n >> m;
    memset(iA, 0, sizeof(iA));
    memset(iB, 0, sizeof(iB));
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    memset(ax, 0, sizeof(ax));
    memset(ay, 0, sizeof(ay));
    memset(bx, 0, sizeof(bx));
    memset(by, 0, sizeof(by));
    resx = resy = 0;
    rep(i, 0, m) {
      cin >> c >> x >> y;
      if (c == 'x' || c == 'o') {
//        a[x][y] = 1;
        ax[x] = true;
        ay[y] = true;
        resx ++;
        iA[x][y] = 1;
      }
      if (c == '+' || c == 'o') {
//        b[x][y] = 1;
        bx[x + y] = true;
        by[y - x + MAXN] = true;
        resx ++;
        iB[x][y] = 1;
      }
    }
    rep(i, 1, n + 1)
      rep(j, 1, n + 1)
        if (!ax[i] && !ay[j]) {
          a[i][j] = 1;
          ax[i] = true;
          ay[j] = true;
        }
    x1 = 1; y1 = 1;
    x2 = n; y2 = n;
    while (true) {
      x = x1; y = y1;
      while (x > 0) {
        if (!bx[x + y] && !by[y - x + MAXN]) {
          b[x][y] = 1;
          bx[x + y] = true;
          by[y - x + MAXN] = true;
        } 
        x --; y ++;
      }
      x1 ++;
      if (x1 > n)
        break;

      x = x2; y = y2;
      while (y <= n) {
        if (!bx[x + y] && !by[y - x + MAXN]) {
          b[x][y] = 1;
          bx[x + y] = true;
          by[y - x + MAXN] = true;
        }
        x --; y ++;
      }
      y2 --;
    }
    rep(i, 1, n + 1) {
      rep(j, 1, n + 1) {
        if (a[i][j] || b[i][j]) {
          resy ++;
          resx += (a[i][j] + b[i][j]);
        }
      }
    }
    cout << "Case #" << t << ": ";
    cout << resx << " " << resy << endl;
    rep(i, 1, n + 1) {
      rep(j, 1, n + 1) {
        if ((a[i][j] || b[i][j]) && (a[i][j] + iA[i][j] + b[i][j] + iB[i][j]) == 2) {
          cout << "o " << i << " " << j << endl;
        } else if (a[i][j]) {
          cout << "x " << i << " " << j << endl;
        } else if (b[i][j]) {
          cout << "+ " << i << " " << j << endl;
        }
      }
    }
  }
  return 0;
}
