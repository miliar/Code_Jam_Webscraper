#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int n, p;
    cin >> n >> p;
    vector<int> a(p);
    for (int i = 0; i < n; i++) {
      int t;
      cin >> t;
      t %= p;
      a[t]++;
    }
    vector<int> b;
    if (p == 2) {
      for (int i = 0; i < a[0]; i++) {
        b.push_back(0);
      }
      for (int i = 0; i < a[1]; i++) {
        b.push_back(1);
      }
    }
    if (p == 3) {
      for (int i = 0; i < a[0]; i++) {
        b.push_back(0);
      }
      for (int i = 0; i < min(a[1], a[2]); i++) {
        b.push_back(1);
        b.push_back(2);
      }
      for (int i = min(a[1], a[2]); i < max(a[1], a[2]); i++) {
        b.push_back(1);
      }
    }
    if (p == 4) {
      for (int i = 0; i < a[0]; i++) {
        b.push_back(0);
      }
      for (int i = 0; i < a[2] / 2 * 2; i++) {
        b.push_back(2);
      }
      for (int i = 0; i < min(a[1], a[3]); i++) {
        b.push_back(1);
        b.push_back(3);
      }
      if (a[2] & 1) {
        b.push_back(2);
      }
      for (int i = min(a[1], a[3]); i < max(a[1], a[3]); i++) {
        b.push_back(1);
      }
    }
    int ans = 0, now = 0;
    for (auto x : b) {
      if (now == 0) ans++;
      now = (now + p - x) % p;
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
