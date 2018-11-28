/*
 *
 * CodeJam 2017 - Round 1A
 * Problem 1
 *
 */

#include <bits/stdc++.h>

using namespace std;

struct Region { int s_row, s_col, e_row, e_col; };

bool is_valid(char l, vector<vector<char>>& matrix, int s_row, int s_col, int e_row, int e_col) {
  for (int r = s_row; r <= e_row; ++r) {
    for (int c = s_col; c <= e_col; ++c) {
      if (matrix[r][c] != l && matrix[r][c] != '?') {
        return false;
      }
    }
  }
  return true;
}

int main() {
  int t;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    printf("Case #%d:\n", i);

    int R, C;
    cin >> R >> C;

    vector<vector<char>> matrix(R, vector<char>(C));

    vector<char> letters;
    unordered_map<char, Region> map;

    for (int r = 0; r < R; ++r) {
      string str;
      cin >> str;
      for (int c = 0; c < C; ++c) {
        matrix[r][c] = str[c];
        if (str[c] == '?') continue;
        if (map.find(str[c]) == map.end()) {
          letters.push_back(str[c]);
          map[str[c]] = Region{r, c, r, c};
        } else {
          map[str[c]].s_row = min(map[str[c]].s_row, r);
          map[str[c]].s_col = min(map[str[c]].s_col, c);
          map[str[c]].e_row = max(map[str[c]].e_row, r);
          map[str[c]].e_col = max(map[str[c]].e_col, c);
        }
      }
    }

    for (char l : letters) {
      for (int r = map[l].s_row; r <= map[l].e_row; ++r) {
        for (int c = map[l].s_col; c <= map[l].e_col; ++c) {
          matrix[r][c] = l;
        }
      }
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        if (matrix[r][c] == '?') {
          for (char l : letters) {
            int s_row = min(map[l].s_row, r);
            int s_col = min(map[l].s_col, c);
            int e_row = max(map[l].e_row, r);
            int e_col = max(map[l].e_col, c);
            if (is_valid(l, matrix, s_row, s_col, e_row, e_col)) {
              matrix[r][c] = l;
              map[l].s_row = s_row;
              map[l].s_col = s_col;
              map[l].e_row = e_row;
              map[l].e_col = e_col;
              break;
            }
          }
        }
      }
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        cout << matrix[r][c];
      }
      cout << endl;
    }
  }

  return 0;
}
