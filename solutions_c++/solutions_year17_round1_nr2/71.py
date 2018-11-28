#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char* argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vector<vector<int>> b(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> b[i][j];
      }
      sort(b[i].begin(), b[i].end());
    }
    int ans = 0;
    vector<int> h(n, 0);
    for (int z = 0;; z++) {
      int flag = 1;
      for (int i = 0; i < n; i++) {
        while (h[i] < m && b[i][h[i]] * 10 < a[i] * z * 9) h[i]++;
        if (h[i] == m) {
          flag = -1;
          break;
        }
        if (b[i][h[i]] * 10 > a[i] * z * 11) {
          flag = 0;
          break;
        }
      }
      if (flag == -1) {
        break;
      }
      if (flag == 1) {
        ans++;
        for (auto& x : h) {
          x++;
        }
        z--;
      }
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
