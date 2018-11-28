#include <bits/stdc++.h>
using namespace std;
using LL = long long;

int a[6], b[6], vis[6];
string s = "ROYGBV";

string get(int a, int b, int cnt) {
  string res = "";
  while (cnt --)
    res += s[a], res += s[b];
  return res;
}

int main() {
  freopen("123.in", "r", stdin);
  freopen("123.out", "w", stdout);
  int T, cas = 0;
  cin >> T;
  while (T --) {
    int n;
    cin >> n;
    for (int i = 0; i < 6; i ++)
      cin >> b[i];
    a[0] = b[0]; a[2] = b[2]; a[4] = b[4];
    string ans = "";
    printf("Case #%d: ", ++ cas);
    if (b[1] > 0) {
      if (b[4] < b[1]) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[4] == b[1] && b[4] + b[1] != n) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[4] == b[1]) {
        puts(get(4, 1, b[4]).c_str());
        continue;
      }
      a[4] = b[4] - b[1];
    }
    if (b[3] > 0) {
      if (b[0] < b[3]) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[0] == b[3] && b[0] + b[3] != n) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[0] == b[3]) {
        puts(get(0, 3, b[0]).c_str());
        continue;
      }
      a[0] = b[0] - b[3];
    }
    if (b[5] > 0) {
      if (b[2] < b[5]) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[2] == b[5] && b[2] + b[5] != n) {
        puts("IMPOSSIBLE");
        continue;
      }
      if (b[2] == b[5]) {
        puts(get(2, 5, b[2]).c_str());
        continue;
      }
      a[2] = b[2] - b[5];
    }
    memset(vis, 0, sizeof vis);
    int flag = 0;
    while (ans.size() < n) {
      int mx = 0, c = 0;
      for (int i = 0; i < 6; i ++) {
        if (s[i] == ans.back()) continue;
        if (a[i] == mx && ans.size() && s[i] == ans[0]) mx = a[i], c = i;
        if (a[i] > mx) mx = a[i], c = i;
      }
      if (s[c] == ans.back() || a[c] == 0) {
        flag = 1; break;
      }
      if (! vis[c])
        ans += get(c, (c + 3) % 6, b[(c + 3) % 6]), vis[c] = 1;
      ans.push_back(s[c]);
      a[c] --;
    }
    // cout << ans << endl;
    if (ans.size() > 1 && ans[0] == ans.back())
      flag = 1;
    if (flag)
      puts("IMPOSSIBLE");
    else
      printf("%s\n", ans.c_str());
  }
  return 0;
}