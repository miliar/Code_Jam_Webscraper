#include <bits/stdc++.h>
using namespace std;

using ll = long long;

vector <int> substract(vector <int> option, vector <int> a, int cnt) {
  int ans = 0;
  for (int x: option) {
    a[x] -= cnt;
  }
  return a;
}

bool check(vector <int> a) {
  for (int x: a) {
    if (x < 0) {
      return 0;
    }
  }
  return 1;
}

void solve() {
  int n, p;
  cin >> n >> p;
  vector <int> a(p);
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    a[x % p]++;
  }
  if (p == 2) {
    cout << n - a[1] / 2 << endl;
  } else if (p == 3) {
    int ans = 0;
    for (int x = 0; x <= min(a[1], a[2]); ++x) {
      int cur = x + a[0];
      auto rest = a;
      rest[0] = 0;
      rest[1] -= x;
      rest[2] -= x;
      cur += rest[1] / 3;
      rest[1] %= 3;
      cur += rest[2] / 3;
      rest[2] %= 3;
      if (rest[1] && rest[2])
        continue;
      if (rest[1] + rest[2] > 0)
        cur++;
      ans = max(ans, cur);
    }
    cout << ans << endl;
  } else {
    int ans = 0;
    for (int x = 0; x <= a[1]; ++x) {
      for (int y = 0; y <= (a[1] - x) / 2;  ++y) {
        int cur = a[0] + x + y + (a[2] - y) / 2 + (a[3] - x) / 4 + (a[1] - x - 2 * y) / 4;
        auto rest = a;
        rest[0] = 0;
        rest[1] -= x + 2 * y;
        rest[2] -= y;
        rest[3] -= x;
        if (rest[1] < 0 || rest[2] < 0 || rest[3] < 0) {
          continue;
        }
        if (rest[3] && rest[1]) {
          continue;
        }
        if (rest[2] && rest[1] > 1) {
          continue;
        }
        int bla = 0;
        for (int x: rest) {
          bla += x;
        }
        cur += bla ? 1 : 0;
        ans = max(ans, cur);
      }
    }
    cout << ans << endl;
    return;
  }
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
#endif
  cout.precision(10);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}