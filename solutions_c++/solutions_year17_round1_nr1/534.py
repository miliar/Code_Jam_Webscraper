#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 1; i <= n; i++)
#define REP(i, n) for(int i = 0; i < n; i++)
#define MP make_pair
#define FI first
#define SE second
#define VI vector<int>
#define CLR(x) memset(x, 0, sizeof(x))
#define SZ(x) (x.size())
#ifdef QWERTIER
#define err(x) cerr<<x<<endl;
#else
#define err(x)
#endif

char s[100][100];

int main() {
#ifdef QWERTIER
  //freopen("in.txt", "r", stdin);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    printf("Case #%d:\n", kase);
    int n , m;
    scanf("%d%d", &n, &m);
    REP (i, n) {
      scanf("%s", s[i]);
      int lst = 0, lchar = '?';
      REP (j, m) {
        if (isalpha(s[i][j])) {
          for (int k = lst; k < j; k++) {
            s[i][k] = s[i][j];
          }
          lchar = s[i][j];
          lst = j + 1;
        }
      }
      for (int j = lst; j < m; j++) {
        s[i][j] = lchar;
      }
    }
    int lst = 0, lline = -1;
    REP (i, n) {
      if (isalpha(s[i][0])) {
        for (int r = lst; r < i; r++) {
          REP (c, m) {
            s[r][c] = s[i][c];
          }
        }
        lst = i + 1;
        lline = i;
      }
    }
    for (int i = lline + 1; i < n; i++) {
      REP (j, m) {
        s[i][j] = s[lline][j];
      }
    }
    REP (i, n)
      puts(s[i]);
  }
  return 0;
}
