#include <iostream>
#include <vector>
using namespace std;

void solve() {
  double d;
  int n;
  cin >> d >> n;
  vector<double> s(n), v(n);

  vector<int> ind(n);
  for (int i = 0; i < n; ++i) {
    ind[i] = i;
    cin >> s[i] >> v[i];
  }
  //  sort(ind.begin(), ind.end(), [](int i, int j) { return v[i] < v[j]; });
  double ans = 0;
  {
    double vmax = 1e19;
    double vv = vmax;
    for (int j = 0; j < n; ++j) {
      if (v[j] < vmax) {
        vv = min(vv, v[j] * d / (d - s[j]));
      }
    }
    ans = max(vv, ans);
  }
  for (int i = 0; i < n; ++i) {
    double vmax = v[i];
    double vv = vmax;
    for (int j = 0; j < n; ++j) {
      if (v[j] < vmax) {
        vv = min(vv, v[j] * d / (d - s[j]));
      }
    }
    ans = max(vv, ans);
  }
  cout << ans;
}
int main() {
  cout.precision(20);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
