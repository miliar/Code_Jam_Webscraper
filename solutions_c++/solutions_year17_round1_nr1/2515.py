#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> grid;

bool is_empty(int l, int r, int u, int d, int _x, int _y) {
  for(int x = l; x <= r; ++x) {
    for(int y = u; y <= d; ++y) {
      if(y == _y && x == _x)
        continue;
      if(grid[y][x] != '?')
        return false;
    }
  }
  return true;
}

void fill(int x, int y) {
  int l = x, r = x;
  int u = y, d = y;

  for(l = x - 1; l >= 0 && is_empty(l, r, u, d, x, y); l--)
    ;
  ++l;
  for(r = x + 1; r < grid[0].size() && is_empty(l, r, u, d, x, y); r++)
    ;
  --r;
  for(u = y - 1; u >= 0 && is_empty(l, r, u, d, x, y); u--)
    ;
  ++u;
  for(d = y + 1; d < grid.size() && is_empty(l, r, u, d, x, y); d++)
    ;
  --d;

  for(int _x = l; _x <= r; ++_x) {
    for(int _y = u; _y <= d; ++_y) {
      grid[_y][_x] = grid[y][x];
    }
  }
}

int main(void) {
  int t, tt;
  cin >> tt;

  for(t = 1; t <= tt; ++t) {
    int i, j;
    int x, y;
    int r, c;

    cin >> r;
    cin >> c;

    grid.clear();
    for(y = 0; y < r; ++y) {
      string s;
      cin >> s;
      grid.push_back(s);
    }

    bool work[26];
    for(i = 0; i < 26; ++i) work[i] = true;

    for(y = 0; y < r; ++y) {
      for(x = 0; x < c; ++x) {
        if(grid[y][x] != '?' && work[grid[y][x] - 'A']) {
          fill(x, y);
          work[grid[y][x] - 'A'] = false;
        }
      }
    }

    cout << "Case #" << t << ":" << endl;
    for(y = 0; y < r; ++y) {
      for(x = 0; x < c; ++x) {
        cout << (char)grid[y][x];
      }
      cout << endl;
    }
  }
  return 0;
}

