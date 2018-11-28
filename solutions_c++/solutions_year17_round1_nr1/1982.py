#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <limits>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

int INF = std::numeric_limits<int>().max();
double INFD = std::numeric_limits<double>().max();

double PI = acos(-1);

void Move(int r, int l, int line, int col, vector<pair<int, int>>& moves) {
  vector<pair<int, int>> ps(4);
  ps[0] = make_pair(0, 1);
  ps[1] = make_pair(0, -1);
  ps[2] = make_pair(1, 0);
  ps[3] = make_pair(-1, 0);
  for (auto& p : ps) {
    int next_line = p.first + line, next_col = p.second + col;
    if (0 <= next_line && next_line < r && 0 <= next_col && next_col <= l) {
      moves.push_back(make_pair(next_line, next_col));
    }
  }
}

bool IsGood(vector<vector<char>>& grid, pair<int, int> upper_left,
            pair<int, int> lower_right, char c) {
  int i = upper_left.first;
  while (i <= lower_right.first) {
    int j = upper_left.second;
    while (j <= lower_right.second) {
      if (grid[i][j] != c && grid[i][j] != '?') {
        return false;
      }
      j++;
    }
    i++;
  }
  return true;
}

void OrderlyDFS(vector<vector<char>>& grid, int r_line, int r_col) {
  char desired = grid[r_line][r_col];
  pair<int, int> upper_left = make_pair(r_line, r_col),
                 lower_right = upper_left;
  stack<pair<int, int>> q;
  grid[upper_left.first][upper_left.second] = '?';
  q.push(upper_left);
  while (q.size()) {
    auto p = q.top();
    q.pop();
    if (upper_left.first <= p.first && p.first <= lower_right.first &&
        upper_left.second <= p.second && p.second <= lower_right.second) {
      grid[p.first][p.second] = desired;
    } else if (IsGood(grid, make_pair(min(upper_left.first, p.first),
                                      min(upper_left.second, p.second)),
                      make_pair(max(lower_right.first, p.first),
                                max(lower_right.second, p.second)),
                      desired)) {
      upper_left = make_pair(min(upper_left.first, p.first),
                             min(upper_left.second, p.second));
      lower_right = make_pair(max(lower_right.first, p.first),
                              max(lower_right.second, p.second));
      grid[p.first][p.second] = desired;
    } else {
      continue;
    }
    vector<pair<int, int>> moves;
    Move(grid.size(), grid[0].size(), p.first, p.second, moves);
    for (auto& m : moves) {
      if (grid[m.first][m.second] == '?') {
        q.push(m);
      }
    }
  }
}

void Print(vector<vector<char>> grid) {
  int i = 0;
  while (i < grid.size()) {
    int j = 0;
    while (j < grid[i].size()) {
      cout << grid[i][j];
      j++;
    }
    cout << endl;
    i++;
  }
}

int main() {
  ios::sync_with_stdio(false);
  int t = 0;
  cin >> t;
  int q = 0;
  while (q < t) {
    int r = 0, c = 0;
    cin >> r >> c;
    vector<vector<char>> grid(r, vector<char>(c));
    vector<pair<int, int>> letters;
    int i = 0;
    for (auto& line : grid) {
      int j = 0;
      for (auto& x : line) {
        cin >> x;
        if (x != '?') {
          letters.push_back(make_pair(i, j));
        }
        j++;
      }
      i++;
    }
    while (true) {
      random_shuffle(letters.begin(), letters.end());
      auto grid2 = grid;
      for (auto& x : letters) {
        OrderlyDFS(grid2, x.first, x.second);
      }
      i = 0;
      bool g = true;
      while (i < r && g) {
        int j = 0;
        while (j < c && g) {
          if (grid2[i][j] == '?') {
            g = false;
          }
          j++;
        }
        i++;
      }
      if (g) {
        grid = grid2;
        break;
      }
    }
    cout << "Case #" << ++q << ":" << endl;
    Print(grid);
  }
  return 0;
}
