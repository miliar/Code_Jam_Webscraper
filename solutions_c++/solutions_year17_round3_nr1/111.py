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

#define N 1010
int n;
#define r first
#define h second
pair<int, int> a[N];
double get_area(int j, int i) {
}
double dp[N][N];

const double PI = acos(-1.0);
typedef pair<int, int> pii;
bool cmp_by_r(const pii &i, const pii &j) {
  return i.r > j.r;
}
int main() {
#ifdef QWERTIER
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    int k;
    scanf("%d%d", &n, &k);
    FOR (i, n) {
      scanf("%d%d", &a[i].r, &a[i].h);
    }
    sort(a+1, a+n+1, cmp_by_r);
    memset(dp, 0, sizeof(dp));
    double ans = 0;
    FOR (i, n) {
      for (int j = 1; j <= min(i, k); j++) {
        if (j == 1)
          dp[i][j] = max(dp[i-1][j], PI * a[i].r * a[i].r + 2*PI*a[i].r*a[i].h);
        else
          dp[i][j] = max(dp[i-1][j-1] + 2*PI*a[i].r*a[i].h, dp[i-1][j]);
      }
      ans = max(ans, dp[i][k]);
    }
    printf("Case #%d: %.15f\n", kase, ans);
  }
  return 0;
}
