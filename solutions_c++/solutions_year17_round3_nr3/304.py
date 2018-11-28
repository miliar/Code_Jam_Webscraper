#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;
typedef long double ld;

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, n, k;
  cin >> T;
  ld u, x;
  vector <ld> v;

  for (int tt = 1; tt <= T; tt++) {
    cin >> n >> k;
    cin >> u;
    v.clear();
    for (int i = 0; i < n; i++) {
      cin >> x;
      v.push_back(x);
    }
    v.push_back(1);
    sort(v.begin(), v.end());
    vector< ld > cur;
    while(u > 0.0) {
      int total = 0;
      for (int i = 0; i < v.size() && v[i] == v[0]; i++) {
        total++;
      }
      if (total == v.size()) break;
      ld diff = v[total] - v[total - 1];
      if (u >= diff * total) {
        u -= diff * total;
        for (int i = 0; i < total; i++) {
          v[i] = v[total];
        }
      } else {
        for (int i = 0; i < total; i++) {
          v[i] += u / total;
        }
        u = 0;
      }
    }
    ld ans = 1.0;
    for (int i = 0; i < v.size(); i++) {
      ans *= v[i];
    }
    cout << "Case #" << tt << ": ";
    cout << fixed << setprecision(10) << ans << endl;
  }

  return 0;
}
