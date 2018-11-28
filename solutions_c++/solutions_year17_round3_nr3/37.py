#include <bits/stdc++.h>
using namespace std;

double solve() {
  int n, k;
  double units;
  cin >> n >> k >> units;
  vector<double> a(n);
  for (auto &p : a)
    cin >> p;
  sort(a.begin(), a.end());
  for (int i = 0; i < n; ++i) {
    double up = i == n - 1 ? 1.0 : a[i + 1];
    double add = min(units / (i + 1), up - a[i]);
    units -= add * (i + 1);
    //cerr << "to first " << i + 1 << " huis add " << add << '\n';
    for (int j = 0; j <= i; ++j) {
      a[j] += add;
    }
  }
  double ans = 1;
  for (auto &p : a)
    ans *= p;
  return ans;
}

int main() {
  int t;
  cin >> t;
  cout << setprecision(15) << fixed;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << '\n';
}