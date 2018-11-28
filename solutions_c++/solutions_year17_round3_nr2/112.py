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
typedef long long LL;


#define N 110
int n, m, l1[N], r1[N], l2[N], r2[N];
int dp[24*70][24*70][2], busy1[24*70], busy2[24*70];
int main() {
#ifdef QWERTIER
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    scanf("%d%d", &n, &m);
    memset(busy1, 0, sizeof(busy1));
    memset(busy2, 0, sizeof(busy2));
    FOR (i, n) {
      scanf("%d%d", &l1[i], &r1[i]);
      for (int j = l1[i]+1; j <= r1[i]; j++)
        busy1[j] = 1;
    }
    FOR (i, m) {
      scanf("%d%d", &l2[i], &r2[i]);
      for (int j = l2[i]+1; j <= r2[i]; j++)
        busy2[j] = 1;
    }
    memset(dp, 0x3f, sizeof(dp));
    dp[0][0][0] = 0;
    FOR (i, 24*60) {
      REP (j, i+1) {
        if (!busy1[i]) {
          dp[i][j][0] = min(j>0?dp[i-1][j-1][0]:100000, (j>0?dp[i-1][j-1][1]:100000) + 1);
        }
        if (!busy2[i]) {
          dp[i][j][1] = min(dp[i-1][j][1], dp[i-1][j][0] + 1);
        }
        //printf("%d %d %d %d\n", i, j, dp[i][j][0], dp[i][j][1]);
      }
    }
    int ans = 1<<30;
    ans = min(ans, min(dp[24*60][12*60][0], dp[24*60][12*60][1] + 1));
    memset(dp, 0x3f, sizeof(dp));
    dp[0][0][1] = 0;
    FOR (i, 24*60) {
      REP (j, i+1) {
        if (!busy1[i]) {
          dp[i][j][0] = min(j>0?dp[i-1][j-1][0]:100000, (j>0?dp[i-1][j-1][1]:100000) + 1);
        }
        if (!busy2[i]) {
          dp[i][j][1] = min(dp[i-1][j][1], dp[i-1][j][0] + 1);
        }
        //printf("%d %d %d %d\n", i, j, dp[i][j][0], dp[i][j][1]);
      }
    }
    ans = min(ans, min(dp[24*60][12*60][0] + 1, dp[24*60][12*60][1]));
    printf("Case #%d: %d\n", kase, ans);
  }
  return 0;
}
