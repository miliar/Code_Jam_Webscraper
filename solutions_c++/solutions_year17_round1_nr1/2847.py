#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

bool is_possible(int r1, int c1, int r2, int c2, char ch, vector<string> &grid) {
  int r = grid.size();
  int c = grid[0].size();

  if (r <= r1 or r <= r2 or c <= c1 or c <= c2) return false;
  if (r1 < 0 or r2 < 0 or c1 < 0 or c2 < 0) return false;

  for (int i = r1; i <= r2; ++i) {
    for (int j = c1; j <= c2; ++j) {
      if (grid[i][j] == ch) continue;
      if (grid[i][j] != '?') return false;
    }
  }

  return true;
}

int put_initial(int r1, int c1, int r2, int c2, char ch, vector<string> &grid) {
  int r = grid.size();
  int c = grid[0].size();

  for (int i = r1; i <= r2; ++i) {
    for (int j = c1; j <= c2; ++j) {
      grid[i][j] = ch;
    }
  }

  return 0;
}


int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ":" << endl;

    int r, c;
    cin >> r >> c;

    vector<string> grid(r);
    for (auto &line : grid) cin >> line;

    vector<int> rows, cols;
    for (int row = 0; row < r; ++row) {
      for (int col = 0; col < c; ++col) {
        if (grid[row][col] != '?') {
          rows.push_back(row);
          cols.push_back(col);
        }
      }
    }

    vector<int> row_1, col_1, row_2, col_2;
    for (int i = 0; i < rows.size(); ++i) {
      int row = rows[i];
      int col = cols[i];

      // up
      int rr = row - 1;
      for (; rr >= 0; --rr) {
        if (grid[rr][col] != '?') break;
        grid[rr][col] = grid[row][col];
      }
      rr++;

      // left
      int cc = col - 1;
      for (; cc >= 0; --cc) {
        if (is_possible(rr, cc, row, col, grid[row][col], grid) == false) break;
        put_initial(rr, cc, row, col, grid[row][col], grid);
      }
      cc++;

      row_1.push_back(rr);
      col_1.push_back(cc);
      row_2.push_back(row);
      col_2.push_back(col);
    }

    for (int i = 0; i < row_1.size(); ++i) {
      int r1 = row_2[i];
      int c1 = col_1[i];
      int r2 = row_2[i];
      int c2 = col_2[i];

      // down
      while (true) {
        r1++; r2++;
        if (is_possible(r1, c1, r2, c2, grid[row_1[i]][col_1[i]], grid) == false) break;
        put_initial(r1, c1, r2, c2, grid[row_1[i]][col_1[i]], grid);
      }
      r1--; r2--;

      r1 = row_1[i];
      c1 = col_2[i];

      // right
      while (true) {
        c1++; c2++;
        if (is_possible(r1, c1, r2, c2, grid[row_1[i]][col_1[i]], grid) == false) break;
        put_initial(r1, c1, r2, c2, grid[row_1[i]][col_1[i]], grid);
      }
    }

    for (auto line : grid) cout << line << endl;
  }

  return 0;
}
