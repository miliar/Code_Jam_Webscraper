#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

struct Board {
  map<int, set<int>> x;
  map<int, set<int>> y;
  map<int, set<int>> c;
  map<int, set<int>> d;
  void add(int _x, int _y) {
    x[_x].insert(_y);
    y[_y].insert(_x);
    c[_x + _y].insert(_x);
    d[_x - _y].insert(_x);
  }
};

void solvePlus(int g, Board& b) {
  for (int i = 0; i < g; ++i) {
    int head = 0;
    int tail = i;
    bool s = true;
    while (head <= tail) {
      int x, y;
      if (s) {
        x = i - head;
        y = head;
        ++head;
      } else {
        x = i - tail;
        y = tail;
        --tail;
      }
      s = !s;
      if (b.c[x + y].empty() && b.d[x - y].empty()) {
        b.add(x, y);
        break;
      }
    }
  }
  for (int i = 1; i < g; ++i) {
    int head = 0;
    int tail = g - i - 1;
    bool s = true;
    while (head <= tail) {
      int x, y;
      if (s) {
        x = g - 1 - head;
        y = i + head;
        ++head;
      } else {
        x = g - 1 - tail;
        y = i + tail;
        --tail;
      }
      s = !s;
      if (b.c[x + y].empty() && b.d[x - y].empty()) {
        b.add(x, y);
        break;
      }
    }
  }
}

void solveCross(int g, Board& b) {
  for (int i = 0; i < g; ++i) {
    for (int j = 0; j < g; ++j) {
      if (b.x[i].empty() && b.y[j].empty()) {
        b.add(i, j);
        break;
      }
    }
  }
}

int main() {
  int n = 0;
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    int g, m;
    scanf("%d %d\n", &g, &m);
    map<int, map<int, char>> orimap;
    Board b1, b2;
    char c;
    int x, y;
    for (int i = 0; i < m; ++i) {
      scanf("%c %d %d\n", &c, &x, &y);
      --x; --y;
      if (c == '+') {
        b1.add(x, y);
      } else if (c == 'x') {
        b2.add(x, y);
      } else {
        b1.add(x, y);
        b2.add(x, y);
      }
      orimap[x][y] = c;
    }

    solvePlus(g, b1);
    solveCross(g, b2);

    int score = 0;
    int count = 0;
    stringstream ss;
    for (int j = 0; j < g; ++j) {
      for (int k = 0; k < g; ++k) {
        auto it1 = b1.x[j].find(k);
        auto it2 = b2.x[j].find(k);
        int t = 0;
        int tcmp = 0;
        char c = orimap[j][k];
        if (c == '+') {
          tcmp = 1;
        } else if (c == 'x') {
          tcmp = 2;
        } else if (c == 'o') {
          tcmp = 3;
        }
        if (b1.x[j].end() != it1) {
          ++score;
          t += 1;
        }
        if (b2.x[j].end() != it2) {
          ++score;
          t += 2;
        }
        if (t != 0 && tcmp != t) {
          ++count;
          if (t == 1) {
            ss << "+";
          } else if (t == 2) {
            ss << "x";
          } else {
            ss << "o";
          }
          ss << " " << j + 1 << " " << k + 1 << endl;
        }
      }
    }

    cout << "Case #" << i + 1 << ": " << score << " " << count << endl;
    cout << ss.str();
  }
}
