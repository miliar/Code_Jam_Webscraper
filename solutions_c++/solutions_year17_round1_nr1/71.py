#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      for (int j = 0; j < m; j++) {
        if (a[i][j] != '?') {
          for (int k = j - 1; k >= 0 && a[i][k] == '?'; k--) {
            a[i][k] = a[i][j];
          }
          for (int k = j + 1; k < m && a[i][k] == '?'; k++) {
            a[i][k] = a[i][j];
          }
        }
      }
    }
    for (int i = 0; i < n; i++) {
      if (a[i][0] != '?') {
        for (int j = i - 1; j >= 0 && a[j][0] == '?'; j--) {
          a[j] = a[i];
        }
        for (int j = i + 1; j < n && a[j][0] == '?'; j++) {
          a[j] = a[i];
        }
      }
    }
    printf("Case #%d:\n", cas);
    for (auto x : a) {
      cout << x << endl;
    }
  }
  return 0;
}
