#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef long double ld;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;
//typedef long long int;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n,k;
    cin >> n >> k;
    vii ts(n);
    vi r(n), h(n);
    for (int i = 0; i < n; ++i) cin >> ts[i].first >> ts[i].second;
    sort(ts.begin(), ts.end());
    for (int i = 0; i < n; ++i) {
      r[i] = ts[i].first; 
      h[i] = ts[i].second;
    }
    vector<vd> d(k, vd(n));
    for (int i = 1; i < k; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int t = 0; t < j; ++t) if (d[i-1][t] > 0 || i == 1) {
          d[i][j] = max(d[i][j], d[i-1][t] + 2 * M_PI * r[t] * h[t]);
        }
      }
    }
    double ans = 0;
    for (int i = 0; i < n; ++i) if (d[k-1][i] > 0 || k == 1) {
      ans = max(ans, d[k-1][i] + 2 * M_PI * r[i] * h[i] + M_PI * r[i] * r[i]);
    }
    printf("%.10lf\n", ans);
  }
  return 0;
}
