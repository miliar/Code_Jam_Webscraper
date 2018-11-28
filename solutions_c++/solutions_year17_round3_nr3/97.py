#include <iostream>
#include <queue>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  std::cout << std::fixed << std::showpoint;
  std::cout << std::setprecision(10);
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,k;
    double u;
    cin >> n >> k >> u;
    vector<double> p(n);
    for (auto& x : p) {
      cin >> x;
    }
    p.push_back(1);

    std::sort(p.begin(), p.end());

    while (u > 1e-9) {
      double m = p.front();
      double q;
      int same = 0;
      for (auto& x : p) {
        if (m + 1e-9 < x) {
          q = x;
          break;
        }
        same++;
      }
      // cout << u << " " << m << " " << q << " " << same << endl;
      double need = q - m;
      double add = min(u / same, need);
      for (int i = 0; i < same; ++i) {
        p[i] += add;
      }
      u -= add * same;
      // break;
    }

    double ans = 1;
    for (auto& x : p) {
      ans *= x;
    }

    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
