#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    int R, C; cin >> R >> C;
    vector<string> grid(R, "");
    for (auto &ro : grid) cin >> ro;
    for (int r = 0; r < R; ++r) {
      char last = '?';
      for (int c = 0; c < C; ++c) {
        if (grid[r][c] == '?') continue;
        last = grid[r][c];
        for (int i = 1; (c-i>=0) && grid[r][c-i] == '?'; ++i) {
          grid[r][c-i] = grid[r][c];
        }
      }
      if (last != '?') {
        for (int i = C - 1; grid[r][i] == '?'; --i) {
          grid[r][i] = last;
        }
      }
    }
    for (int c = 0; c < C; ++c) {
      char last = '?';
      for (int r = 0; r < R; ++r) {
        if (grid[r][c] == '?') continue;
        last = grid[r][c];
        for (int i = 1; (r-i>=0) && grid[r-i][c] == '?'; ++i) {
          grid[r-i][c] = grid[r][c];
        }
      }
      for (int i = R - 1; grid[i][c] == '?'; --i) {
        grid[i][c] = last;
      }
    }
    cout << "Case #" << cas << ":" << endl;
    for (int r = 0; r < R; ++r)
      cout << grid[r] << '\n';
  }
  return 0;
}
