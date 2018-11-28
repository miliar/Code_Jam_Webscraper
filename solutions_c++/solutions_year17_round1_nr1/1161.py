#include <bits/stdc++.h>

using namespace std;



int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T, R, C;
  char grid[32][32];
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": \n";
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
      int idx = -1;
      for (int j = 0; j < C; ++j) {
        cin >> grid[i][j];
        if (grid[i][j] != '?') {
          for (++idx; idx < j; ++idx) {
            grid[i][idx] = grid[i][j];
          }
          idx = j;
        }
      }
      if (idx != -1) {
        for (++idx; idx < C; ++idx) {
          grid[i][idx] = grid[i][idx - 1];
        }
      }
      if (idx == -1 && i > 0) {
        for (int j = 0; j < C; ++j) {
          grid[i][j] = grid[i - 1][j];
        }
      }
    }
    for (int i = R - 1; i >= 0; --i) {
      int idx = R;
      for (int j = C - 1; j >= 0; --j) {
        if (grid[i][j] != '?') {
          for (--idx; idx > j; --idx) {
            grid[i][idx] = grid[i][j];
          }
          idx = j;
        }
      }
      if (idx != R) {
        for (--idx; idx > -1; --idx) {
          grid[i][idx] = grid[i][idx + 1];
        }
      }
      if (idx == R && i < R - 1) {
        for (int j = 0; j < C; ++j) {
          grid[i][j] = grid[i + 1][j];
        }
      }
    }
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        cout << grid[i][j];
      }
      cout << '\n';
    }
  }
}