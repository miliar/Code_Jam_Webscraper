#include <bits/stdc++.h>

using namespace std;

void brute(int n, int k) {
  vector<int> left(n + 2, 0), right(n + 2, n + 1), minls(n + 2), maxls(n + 2);
  vector<bool> occupied(n + 2, false);
  occupied[0] = occupied[n + 1] = true;
  int ans;
  for (int kk = 1; kk <= k; kk++) {
    for (int i = 1; i <= n; i++) {
      if (!occupied[i]) {
        int ls = (i - 1) - (left[i] + 1) + 1, rs = (right[i] - 1) - (i + 1) + 1;
        if (ls < 0) ls = 0;
        if (rs < 0) rs = 0;
        minls[i] = min(ls, rs);
        maxls[i] = max(ls, rs);
      }
    }
    int maxmin = -1;
    for (int i = 1; i <= n; i++) {
      if (!occupied[i]) {
        maxmin = max(maxmin, minls[i]);
      }
    }
    int maxmax = -1, idx;
    for (int i = 1; i <= n; i++) {
      if (!occupied[i] && minls[i] == maxmin) {
        if (maxmax < maxls[i]) {
          maxmax = maxls[i];
          idx = i;
        }
      }
    }
    ans = idx;
    occupied[idx] = true;
    for (int i = idx - 1; i >= 1 && !occupied[i]; i--) {
      right[i] = idx;
    }
    for (int i = idx + 1; i <= n && !occupied[i]; i++) {
      left[i] = idx;
    }
  }
  cout << maxls[ans] << " " << minls[ans] << endl;
}


int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    freopen("c.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum) {
      int n, k;
      cin >> n >> k;
      cout << "Case #" << tnum << ": ";
      brute(n, k);
    }
    return 0;
}
