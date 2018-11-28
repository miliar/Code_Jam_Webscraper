#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int n, k;
    cin >> n >> k;

    multiset <int> parts;
    parts.insert(n);

    int ls, rs;
    while (k--) {
      if (parts.empty()) {
        ls = rs = 0;
        break;
      }

      auto it = parts.end();
      it--;
      int e = *it;
      parts.erase(it);
      if (e%2 == 1) ls = rs = (e-1)/2;
      else {
        ls = e/2;
        rs = e/2 - 1;
      }

      if (ls != 0) parts.insert(ls);
      if (rs != 0) parts.insert(rs);
    }

    cout << "Case #" << t << ": " << max(ls, rs) << " " << min(ls, rs) << "\n";
  }

  return 0;
}
