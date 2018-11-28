#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
  int n, r, o, y, g, b, v;
  cin >> n >> r >> o >> y >> g >> b >> v;
  int A = g, B = v, C = o;
  string ans_a = "";
  for (int i = 0; i < A; ++i) {
    ans_a += "RG";
  }
  string ans_b = "";
  for (int i = 0; i < B; ++i) {
    ans_b += "YV";
  }
  string ans_c = "";
  for (int i = 0; i < C; ++i) {
    ans_c += "BO";
  }
  int X = r - A, Y = y - B, Z = b - C;
  if (X < 0 || Y < 0 || Z < 0) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  if (A * 2 == n) {
    cout << ans_a << endl;
    return;
  }
  if (B * 2 == n) {
    cout << ans_b << endl;
    return;
  }
  if (C * 2 == n) {
    cout << ans_c << endl;
    return;
  }
  if ((A > 0 && !X) || (B > 0 && !Y) || (C > 0 && !Z)) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  for (int xy = 0; xy <= y; ++xy) {
    int xz = (X - xy);
    if (xz > Z) {
      continue;
    }
    int yz = min(Y - xy, Z - xz);
    int rest_z = Z - yz - xz;
    int rest_y = Y - xy - yz;
    if (rest_z > xy || rest_y > xz) {
      continue;
    }
    string ans;
    for (int i = 0; i < xy; ++i) {
      ans += "RY";
      if (rest_z > 0) {
        rest_z--;
        ans += "B";
      }
    }
    for (int i = 0; i < xz; ++i) {
      ans += "RB";
      if (rest_y > 0) {
        ans += "Y";
        rest_y--;
      }
    }
    for (int i = 0; i < yz; ++i) {
      if (ans.back() == 'Y') {
        ans += "BY";
      } else {
        ans += "YB";
      }
    }
    
    for (int i = 0; i < ans.size(); ++i) {
      if (ans[i] == 'R') {
        ans = ans.substr(0, i) + ans_a + ans.substr(i, ans.size());
        break;
      }
    }
    for (int i = 0; i < ans.size(); ++i) {
      if (ans[i] == 'Y') {
        ans = ans.substr(0, i) + ans_b + ans.substr(i, ans.size());
        break;
      }
    }
    for (int i = 0; i < ans.size(); ++i) {
      if (ans[i] == 'B') {
        ans = ans.substr(0, i) + ans_c + ans.substr(i, ans.size());
        break;
      }
    }
    cout << ans << endl;
    return;
  }
  cout << "IMPOSSIBLE" << endl;
  return;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  cout.precision(10);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}