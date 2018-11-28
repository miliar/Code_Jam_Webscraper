#include <bits/stdc++.h>

#define all(x) x.begin(),x.end()
using namespace std;

typedef long long ll;
typedef long double ld;

int run() {
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    ll d, n;
    cin >> d >> n;
    vector<pair<ll, ll>> mas(n);
    for (int i = 0; i < n; ++i) {
      cin >> mas[i].first >> mas[i].second;
    }
    ld l = 0;
    ld r = 1e18;
    for (int i = 0; i < 1000; ++i) {
      ld m = (l + r) / 2;
      bool iscan = true;
      for (int j = 0; j < n; ++j) {
        if (m > mas[j].second) {
          ld myt = mas[j].first / (m - mas[j].second);
          if (myt * m < d) iscan = false;
        }
      }
      if (iscan) l = m;
      else r = m;
    }
    cout << "Case #" << q + 1 << ": " << fixed << setprecision(7) << l << endl;
  }
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  run();
  return 0;
}