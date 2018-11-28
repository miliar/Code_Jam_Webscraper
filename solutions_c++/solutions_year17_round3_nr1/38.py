#include <bits/stdc++.h>
using namespace std;

double const PI = acos(-1.0);

double solve() {
  int n, k;
  cin >> n >> k;
  vector<pair<int, int>> a(n);
  for (auto& p : a)
    cin >> p.first >> p.second;
  sort(a.begin(), a.end());
  multiset<double> hs;
  double sum = 0;
  double ans = 0;
  for (auto p : a) {
    double R = p.first, H = p.second;
    double ar = 2 * PI * R * H;
    if ((int)hs.size() == k - 1) {
      double cur = PI * R * R + sum + ar;
      ans = max(ans, cur);
    }
    hs.insert(ar);
    sum += ar;
    while ((int)hs.size() > k - 1) {
      sum -= *hs.begin();
      hs.erase(hs.begin());
    }
  }
  return ans;
}

int main() {
  int t;
  cin >> t;
  cout << setprecision(15) << fixed;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << '\n';
}
