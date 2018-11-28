#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>

typedef long long ll;

using namespace std;

string grid[30];
bool vis[30][30];
int R, C;

void fill(char ch, int r, int c) {
  if (r < 0 || c < 0 || r >= R || c >= C || grid[r][c] != '?') return;
  grid[r][c] = ch;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> R >> C;
    memset(vis, 0, sizeof vis);
    for (int i = 0; i < R; i++) {
      cin >> grid[i];
    }

    for (int c = 0; c < C; c++) {
      for (int r = 0; r < R; r++) {
        if (grid[r][c] != '?') {
          fill(grid[r][c], r - 1, c);
          fill(grid[r][c], r + 1, c);
        }
      }
      for (int r = R - 1; r >= 0; r--) {
        if (grid[r][c] != '?') {
          fill(grid[r][c], r - 1, c);
          fill(grid[r][c], r + 1, c);
        }
      }
    }

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] != '?') {
          fill(grid[r][c], r, c - 1);
          fill(grid[r][c], r, c + 1);
        }
      }
      for (int c = C - 1; c >= 0; c--) {
        if (grid[r][c] != '?') {
          fill(grid[r][c], r, c - 1);
          fill(grid[r][c], r, c + 1);
        }
      }
    }

    cout << "Case #" << tt << ":" << endl;
    for (int i = 0; i < R; i++) {
      cout << grid[i] << endl;
    }
  }

  return 0;
}
