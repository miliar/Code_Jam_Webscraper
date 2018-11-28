#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> grid;
map<char, bool> m;
int r, c;
void extend(int a, int b) {
  int up = a, down = a;
  int left = b, right = b;
  char who = grid[a][b];
  while (1) {
    // cout << up << ' ' << down << ' ' << left << ' ' << right << endl;
    bool flag = true;
    int cnt = 0;
    if (left > 0) {
      for (int i = up; i <= down; i++) {
        for (int j = left-1; j <= right; j++) {
          if (grid[i][j] != '?' && grid[i][j] != who) {
            flag = false;
            break;
          }
        }
      }
      if (flag) {
        left--;
        cnt++;
      }
    }
    if (right < c - 1) {
      flag = true;
      for (int i = up; i <= down; i++) {
        for (int j = left; j <= right+1; j++) {
          if (grid[i][j] != '?' && grid[i][j] != who) {
            flag = false;
            break;
          }
        }
      }
      if (flag) {
        right++;
        cnt++;
      }
    }
    if (up > 0) {
      flag = true;
      for (int i = up-1; i <= down; i++) {
        for (int j = left; j <= right; j++) {
          if (grid[i][j] != '?' && grid[i][j] != who) {
            flag = false;
            break;
          }
        }
      }
      if (flag) {
        up--;
        cnt++;
      }
    }
    if (down < r - 1) {
      flag = true;
      for (int i = up; i <= down+1; i++) {
        for (int j = left; j <= right; j++) {
          if (grid[i][j] != '?' && grid[i][j] != who) {
            flag = false;
            break;
          }
        }
      }
      if (flag) {
        down++;
        cnt++;
      }
    }
    // cout << up << ' ' << down << ' ' << left << ' ' << right << endl;
    // cout << "---" << who << endl;
    if (cnt == 0) {
      break;
    }
  }
  for (int i = up; i <= down; i++) {
    for (int j = left; j <= right; j++) {
      grid[i][j] = who;
    }
  }
}

int main() {
  int t;
  cin >> t;
  for (int _ = 1; _ <= t; _++) {
    cout << "Case #" << _ << ":" << endl;
    grid.clear();
    m.clear();
    cin >> r >> c;
    grid.resize(r);
    for (int i = 0; i < r; i++) {
      cin >> grid[i];
      // cout << grid[i] << endl;
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] != '?' && m.find(grid[i][j]) == m.end()) {
          extend(i, j);
          m[grid[i][j]] = true;
        }
      }
    }
    // cout << "-----" << endl;
    for (int i = 0; i < r; i++) {
      cout << grid[i] << endl;
    }
  }
}
