#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
#include <utility>

using namespace std;

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int n, k;
    cin >> n >> k;

    int u;
    multiset<int> p;

    double u_t;
    cin >> u_t;
    u = round (u_t * 10000);

    for (int i = 0; i < n; ++i) {
      double p_t;
      cin >> p_t;

      p.insert(round(p_t * 10000));
    }

    if (n == 1) {
      int val = *p.begin() + u;
      p.erase(p.begin());
      p.insert(val);
    } else {
      while (u > 0) {
        auto c = p.begin();
        auto n = c;
        ++n;
        if (*n == *c) {
          int val = *c + 1;
          p.erase(c);
          p.insert(val);
          u -= 1;
        } else {
          int diff = min(u, *n - *c);
          int val = *c + diff;
          p.erase(c);
          p.insert(val);
          u -= diff;
        }
      }
    }

    double out = 1.;

    for (auto& e: p) {
      double v = e / 10000.;
      out = out * v;
    }


    cout << "Case #" << test << ": " << setprecision(15) << out << endl;
  }
}
