#include <bits/stdc++.h>

using namespace std;

const int N = 150;

int a[N];

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n, p;
    cin >> n >> p;
    for (int i = 0; i < n; ++i) cin >> a[i];
    int ans;
    if (p == 2) {
      int par = 0, imp = 0;
      for (int i = 0; i < n; ++i) (a[i] % 2 == 0 ? par : imp)++;
      ans = par + (imp + 1) / 2;
    } else if (p == 3) {
      int z = 0, u = 0, d = 0;
      for (int i = 0; i < n; ++i) {
        if (a[i] % 3 == 0) ++z;
        if (a[i] % 3 == 1) ++u;
        if (a[i] % 3 == 2) ++d;
      }
      ans = z;
      int m = min(u, d);
      ans += m;
      u -= m;
      d -= m;
      ans += (u + 2) / 3 + (d + 2) / 3;
    } else if (p == 4) {
      vector<int> v(4, 0);
      for (int i = 0; i < n; ++i) {
        v[a[i] % 4]++;
      }
      ans = v[0];
      int parelles = v[2] / 2;
      ans += parelles;
      v[2] -= parelles * 2;
      int m = min(v[1], v[3]);
      ans += m;
      v[1] -= m;
      v[3] -= m;
      int rem = max(v[1], v[3]);
      int par = v[2];
      if (par == 1 and rem >= 2) {
        ++ans;
        rem -= 2;
        --par;
      }
      if (par == 1) ++ans;
      else ans += (rem + 3) / 4;
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
}
