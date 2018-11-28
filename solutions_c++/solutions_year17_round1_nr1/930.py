#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int r, c;
    cin >> r >> c;
    vector<string> g(r);
    for (auto& row : g) cin >> row;

    for (int i = 0; i < r; i++) {
      char last = '?';
      for (int j = 0; j < c; j++) {
        if (g[i][j] != '?') {
          last = g[i][j];
          for (int k = j - 1; k >= 0 and g[i][k] == '?'; k--) g[i][k] = g[i][j];
        }
      }

      for (int k = c - 1; k >= 0 and g[i][k] == '?'; k--) g[i][k] = last;
    }

    for (int j = 0; j < c; j++) {
      char last = '?';
      for (int i = 0; i < r; i++) {
        if (g[i][j] != '?') {
          last = g[i][j];
          for (int k = i - 1; k >= 0 and g[k][j] == '?'; k--) g[k][j] = g[i][j];
        }
      }

      for (int k = r - 1; k >= 0 and g[k][j] == '?'; k--) g[k][j] = last;
    }

    cout << "Case #" << tc << ":\n";
    for (int i = 0; i < r; i++) cout << g[i] << '\n';
  }

}
