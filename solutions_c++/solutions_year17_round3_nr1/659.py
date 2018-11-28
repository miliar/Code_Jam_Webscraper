#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

const int maxn = 1005;
int mark[maxn][maxn];
double dp[maxn][maxn];

double f(int i, int j, vector<double> &r, vector<double> &h) {
  int n = r.size();

  if (i == n or j == 0) {
    return 0;
  }

  if (mark[i][j] == 0) {
    mark[i][j] = 1;
    double a = f(i + 1, j, r, h);
    double b = r[i] * h[i] + f(i + 1, j - 1, r, h);
    dp[i][j] = max(a, b);
  }

  return dp[i][j];
}

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    int n, k;
    cin >> n >> k;

    vector<double> r(n), h(n);
    for (int i = 0; i < n; ++i) cin >> r[i] >> h[i];

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (r[i] < r[j]) {
          swap(r[i], r[j]);
          swap(h[i], h[j]);
        }
      }
    }

    memset(mark, 0, sizeof mark);

    double ans = 0;
    for (int i = 0; i < n; ++i) {
      double sum_rh = r[i] * h[i] + f(i + 1, k - 1, r, h);
      double tmp = M_PI * r[i] * r[i] + 2 * M_PI * sum_rh;
      ans = max(ans, tmp);
    }

    cout << fixed << setprecision(9) << ans << endl;
  }

  return 0;
}
