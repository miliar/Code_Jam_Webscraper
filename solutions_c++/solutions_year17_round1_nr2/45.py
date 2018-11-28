#include <bits/stdc++.h>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    cout << "Case #" << ca << ": ";
    int n, p;
    cin >> n >> p;
    vector<ll> r(n);
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }
    vector<vector<ll> > q(n, vector<ll>(p));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> q[i][j];
      }
      sort(q[i].begin(), q[i].end());
    }
    vector<ll> ind(n, 0);
    int ans = 0;
    ll servings = 1;
    while (true) {
      bool done = false;
      for (int i = 0; i < n; ++i) {
        ll min_q = (90 * servings * r[i] + 99) / 100;
        while (ind[i] < p && q[i][ind[i]] < min_q) {
          ++ind[i];
        }
        if (ind[i] == p) {
          done = true;
        }
      }
      if (done) {
        break;
      }

      bool kit_ok = true;
      ll next_servings = servings + 1;
      for (int i = 0; i < n; ++i) {
        ll max_q = 110 * servings * r[i] / 100;
        if (q[i][ind[i]] > max_q) {
          kit_ok = false;
        }
        next_servings = max(next_servings, q[i][ind[i]] * 100 / (110 * r[i]));
      }
      if (kit_ok) {
        ++ans;
        for (int i = 0; i < n; ++i) {
          ++ind[i];
        }
      } else {
        servings = next_servings;
      }
    }
    cout << ans << endl;
  }
}
