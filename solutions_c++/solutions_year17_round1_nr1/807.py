#include <iostream>
#include <string>
#include <vector>
using namespace std;

void print(vector<string>& grid) {
  for (const auto& row : grid) {
    cout << row << endl;
  }
}

void solve(vector<string>& grid) {
  int m = grid.size(), n = grid[0].size();
  for (int i = 0; i < m; i++) {
    char last = '?';
    for (int j = 0; j < n; j++) {
      if (grid[i][j] != '?') {
        last = grid[i][j];
      }
      grid[i][j] = last;
    }
  }

  for (int i = 0; i < m; i++) {
    char last = '?';
    for (int j = n - 1; j >= 0; j--) {
      if (grid[i][j] != '?') {
        last = grid[i][j];
      }
      grid[i][j] = last;
    }
  }

  int not_empty_row = -1;
  for (int i = 0; i < m; i++) {
    if (grid[i][0] != '?') {
      not_empty_row = i;
    } else if (not_empty_row != -1) {
      grid[i] = grid[not_empty_row];
    }
  }

  not_empty_row = m;
  for (int i = m - 1; i >= 0; i--) {
    if (grid[i][0] != '?') {
      not_empty_row = i;
    } else if (not_empty_row != m) {
      grid[i] = grid[not_empty_row];
    }
  }

  for (const auto& row : grid) {
    cout << row << endl;
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":" << endl;
    int m, n;
    cin >> m >> n;
    vector<string> grid(m);
    for (int i = 0; i < m; i++) {
      cin >> grid[i];
    }
    solve(grid);
  }
  return 0;
}