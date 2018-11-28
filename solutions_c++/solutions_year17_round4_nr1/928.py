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


#define N 110
int a[N], dp[N][N][N][4], n, p, cnt[4];
void upd(int &x, int nx) {
  x = max(x, nx);
}
int main() {
#ifdef QWERTIER
  freopen("in.txt", "r", stdin);
  // freopen("A-small-attempt0.in", "r", stdin);
  // freopen("A-small-attempt0.out", "w", stdout);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    printf("Case #%d: ", kase);
    scanf("%d%d", &n, &p);
    FOR (i, n) {
      scanf("%d", &a[i]);
    }
    memset(dp, 0, sizeof(dp));
    memset(cnt, 0, sizeof(cnt));
    FOR (i, n) {
      cnt[a[i]%p]++;
    }
    dp[0][0][0][0] = 0;
    for (int i = 0; i <= cnt[1]; i++) {
      for (int j = 0; j <= cnt[2]; j++) {
        for (int k = 0; k <= cnt[3]; k++) {
          for (int l = 0; l < p; l++) {
            if (i + j + k + l == 0)
              continue;
            if (i > 0)
              upd(dp[i][j][k][l], dp[i-1][j][k][((l-1)%p+p)%p]);
            if (j > 0)
              upd(dp[i][j][k][l], dp[i][j-1][k][((l-2)%p+p)%p]);
            if (k > 0)
              upd(dp[i][j][k][l], dp[i][j][k-1][((l-3)%p+p)%p]);
            if (l == 0)
              dp[i][j][k][l]++;
          }
        }
      }
    }
    printf("%d\n", cnt[0] + dp[cnt[1]][cnt[2]][cnt[3]][0]);
  }
  return 0;
}
