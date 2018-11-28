#include <iostream>
#include <map>
#include <vector>

using namespace std;


class Rec {
public:
  Rec () {}
  Rec (int x, int y) : lux(x), luy(y), rdx(x), rdy(y) {}

  int lux, luy, rdx, rdy;

  void update(int x, int y) {
    lux = min(x, lux);
    luy = min(y, luy);

    rdx = max(x, rdx);
    rdy = max(y, rdy);
  }

  void fill(vector<string> &grid, char c) {
    for (int x = lux; x <= rdx; x++) {
      for (int y = luy; y <= rdy; y++) {
        grid[x][y] = c;
      }
    }
  }

  bool expand(vector<string> &grid, char c, int dx, int dy) {
    if (dx != 0) {
      int x = 0;
      if (dx > 0) x = rdx+dx;
      if (dx < 0) x = lux+dx;

      if (x < 0 || x >= int(grid.size())) return false;

      for (int y = luy; y <= rdy; y++) {
        if (grid[x][y] != '?') return false;
      }

      this->update(x, luy);
      for (int y = luy; y <= rdy; y++) {
        grid[x][y] = c;
      }
    }
    if (dy != 0) {
      int y = 0;
      if (dy > 0) y = rdy+dy;
      if (dy < 0) y = luy+dy;

      if (y < 0 || y >= int(grid[0].size())) return false;

      for (int x = lux; x <= rdx; x++) {
        if (grid[x][y] != '?') return false;
      }

      this->update(lux, y);
      for (int x = lux; x <= rdx; x++) {
        grid[x][y] = c;
      }
    }

    return true;
  }
};

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int R, C;
    cin >> R >> C;

    vector<string> ans;
    map<char, Rec> amap;

    for (int i = 0; i < R; i++) {
      string input;
      cin >> input;

      ans.push_back(input);
      for (int j = 0; j < C; j++) {
        if (input[j] == '?') continue;
        if (amap.count(input[j])) {
          amap[input[j]].update(i, j);
        }
        else {
          amap[input[j]] = Rec(i, j);
        }
      }
    }

    for (auto &r : amap) {
      r.second.fill(ans, r.first);
    }

    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1};
    for (auto &r : amap) {
      while (true) {
        bool changed = false;
        for (int i = 0; i < 4; i++) {
          bool res = r.second.expand(ans, r.first, dx[i], dy[i]);
          changed |= res;
        }
        if (!changed) break;
      }
    }

    cout << "Case #" << t << ":" << endl;

    for (int i = 0; i < R; i++) {
      cout << ans[i] << endl;
    }
  }
  return 0;
}
