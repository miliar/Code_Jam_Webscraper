#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <iomanip>

using namespace std;

const double pi = 3.141592653589793;

int main() {
  std::cout << std::fixed << std::showpoint;
  std::cout << std::setprecision(10);
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,k;
    cin >> n >> k;
    vector<pair<int,int>> a;
    a.resize(n);
    for (auto& x : a) {
      cin >> x.first >> x.second;
    }
    sort(a.begin(), a.end());

    vector<vector<double>> d;
    d.assign(n, vector<double>(k+1, 0.0));

    for (int i = 0; i < n; ++i) {
      double ss = 2 * pi * a[i].second * a[i].first;
      for (int j = 1; j <= k; ++j) {
        if (j == 1) {
          d[i][j] = ss;
        } else {
          for (int s = 0; s < i; ++s) {
            d[i][j] = max(d[i][j], ss + d[s][j-1]);
          }
        }
      }
    }

    double ans = 0;
    for (int i = 0; i < n; ++i) {
      ans = max(ans, pi * a[i].first * a[i].first + d[i][k]);
    }

    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
