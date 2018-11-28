#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 30;

int n,m;
char s[N][N];

inline void solve () {
  scanf ("%d %d", &n, &m);
  for (int i = 0;i < n;i ++) {
    scanf ("%s", s[i]);
  }

  for (int i = 0;i < n;i ++) {
    for (int j = 0;j < m;j ++) {
      if (s[i][j] != '?') {
        int l,r;
        for (int l = j - 1;l >= 0;l --) {
          if (s[i][l] == '?') {
            s[i][l] = s[i][j];
          } else {
            break;
          }
        }
        l ++;
        for (int r = j + 1;r < m;r ++) {
          if (s[i][r] == '?') {
            s[i][r] = s[i][j];
          } else {
            break;
          }
        }
        r --;
      }
    }
  }

  for (int i = n - 2;i >= 0;i --) {
    for (int j = 0;j < m;j ++) {
      if (s[i][j] == '?') {
        s[i][j] = s[i + 1][j];
      }
    }
  }

  for (int i = 1;i < n;i ++) {
    for (int j = 0;j < m;j ++) {
      if (s[i][j] == '?') {
        s[i][j] = s[i - 1][j];
      }
    }
  }

  for (int i = 0;i < n;i ++) {
    printf ("%s\n", s[i]);
  }
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d:\n", i);
    solve ();
  }
}
