/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/

#include <bits/stdc++.h>

using namespace std;

struct mobil {
  double r, h;
};

int n, k;
mobil m[1004];
double dp[1004][1004][2];

const double PI = acos(-1);

bool operator> (const mobil& x, const mobil& y) {
  return (x.r > y.r) || ((x.r == y.r) && (x.h > y.h));
}

int main(int argc, char const *argv[]) {
  int tc;
  scanf("%d", &tc);
  for (int cs = 0; cs < tc; ++cs)
  {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i)
    {
      scanf("%lf%lf", &m[i].r, &m[i].h);
    }

    sort(m, m+n, greater<mobil>());
    memset(dp, 0, sizeof dp);

    dp[0][1][1] = PI * m[0].r * m[0].r + 2 * PI * m[0].r * m[0].h;
    // cout << dp[0][1][1] << '\n';
    // cout << dp[i][j][0] << "," << dp[i][j][1] << '\t';
    for (int i = 1; i < n; ++i)
    {
      for (int j = 0; j <= i + 1; ++j)
      {
        dp[i][j][0] = max(max(dp[i-1][j][0], dp[i-1][j][1]), dp[i][j][0]);
        if (j) {
          double tmp = dp[i][j-1][0];
          if (tmp == 0) {
            tmp += PI * m[i].r * m[i].r;
          }
          // tmp = max(tmp, dp[i-1][j][0]);
          dp[i][j][1] = max(dp[i][j][1], tmp + 2 * PI * m[i].r * m[i].h);
        }
        // cout << dp[i][j][0] << "," << dp[i][j][1] << '\t';
      }
      // cout << '\n';
    }

    double ans = 0.0;
    for (int i = 0; i < n; ++i)
    {
      ans = max(ans, dp[i][k][1]);
    }
    printf("Case #%d: %.12lf\n", cs+1, ans);
  }
  return 0;
}
