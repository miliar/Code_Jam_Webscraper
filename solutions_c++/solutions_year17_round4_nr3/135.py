#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef pair<int,int> pii;

int r, c;
char f[55][55];
vector<vector<int>> g, gt;

int vars[55][55][2];
int valid[205];
vector<pair<int, int>> pos;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};
vector<bool> used;
vector<int> order, comp;

bool Trace(int i, int j, int idx, int dir) {
  if (i < 0 || i >= r || j < 0 || j >= c) {
    return true;
  }
  if (f[i][j] == '|' || f[i][j] == '-') {
    return false;
  } else if (f[i][j] == '.') {
    if (vars[i][j][0] == -1) {
      vars[i][j][0] = idx;
    } else {
      vars[i][j][1] = idx;
    }
  } else if (f[i][j] == '#') {
    return true;
  } else if (f[i][j] == '/') {
    if (dir == 0) {
      dir = 3;
    } else if (dir == 1) {
      dir = 2;
    } else if (dir == 2) {
      dir = 1;
    } else {
      dir = 0;
    }
  } else if (f[i][j] == '\\') {
    if (dir == 0) {
      dir = 1;
    } else if (dir == 1) {
      dir = 0;
    } else if (dir == 2) {
      dir = 3;
    } else {
      dir = 2;
    }
  }
  i += dx[dir];
  j += dy[dir];
  return Trace(i, j, idx, dir);
}


void DFS1(int v) {
  used[v] = true;
  for (int i = 0; i < g[v].size(); ++i) {
    int to = g[v][i];
    if (!used[to]) {
      DFS1(to);
    }
  }
  order.push_back(v);
}

void DFS2(int v, int cl) {
  comp[v] = cl;
  for (int i = 0; i< gt[v].size(); ++i) {
    int to = gt[v][i];
    if (comp[to] == -1) {
      DFS2(to, cl);
    }
  }
}

void Solve() {
  memset(f, 0, sizeof f);
  memset(valid, 0, sizeof valid);
  memset(vars, -1, sizeof vars);
  g.clear();
  gt.clear();
  order.clear();
  pos.clear();
  cin >> r >> c;
  for (int i = 0; i < r; ++i) {
    cin >> f[i];
  }
  bool fail = false;
  int idx = 0;
  for (int i = 0; i < r && !fail; ++i) {
    for (int j = 0; j < c && !fail; ++j) {
      if (f[i][j] == '|' || f[i][j] == '-') {
        pos.emplace_back(i, j);
        pos.emplace_back(i, j);
        vars[i][j][0] = idx;
        bool can1 = Trace(i - 1, j, idx, 0) && Trace(i + 1, j, idx, 2);
        valid[idx] = can1;
        ++idx;
        vars[i][j][1] = idx;
        bool can2 = Trace(i, j - 1, idx, 1) && Trace(i, j + 1, idx, 3);
        valid[idx] = can2;
        ++idx;
        if (!can1 && !can2) {
          fail = true;
        }
      }
    }
  }

  g.resize(idx);
  gt.resize(idx);
  for (int i = 0; i < r && !fail; ++i) {
    for (int j = 0; j < c && !fail; ++j) {
      if (f[i][j] == '.') {
        if (vars[i][j][0] == -1) {
          fail = true;
        } else {
          // Build 2-SAT problem definition
          if (vars[i][j][1] == -1) {
            g[vars[i][j][0] ^ 1].push_back(vars[i][j][0]);
          } else {
            g[vars[i][j][0] ^ 1].push_back(vars[i][j][1]);
            g[vars[i][j][1] ^ 1].push_back(vars[i][j][0]);
          }
        }
      }
    }
  }
  for (int i = 0; i < idx; ++i) {
    if (!valid[i]) {
      g[i].push_back(i ^ 1);
    }
  }
  
  for (int i = 0; i < idx; ++i) {
    for (int j = 0; j < g[i].size(); ++j) {
      gt[g[i][j]].push_back(i);
    }
  }

  // Solve 2-SAT
  used.assign(idx, false); 
  for (int i = 0; i < idx; ++i) {
    if (!used[i]) {
      DFS1(i);
    }
  }

  comp.assign(idx, -1);
  for (int i = 0, j = 0; i < idx; ++i) {
    int v = order[idx - i - 1];
    if (comp[v] == -1) {
      DFS2(v, j++);
    }
  }

  for (int i = 0; i < idx; ++i) {
    if (comp[i] == comp[i ^ 1]) {
      fail = true;
    }
  }
  for (int i = 0; i < idx; i += 2) {
    int ans = comp[i] > comp[i ^ 1] ? i : (i ^ 1);
    if (ans % 2 == 0) {
      f[pos[ans].first][pos[ans].second] = '|';
    } else {
      f[pos[ans].first][pos[ans].second] = '-';
    } 
  }
  if (fail) {
    cout << "IMPOSSIBLE\n";
  } else {
    cout << "POSSIBLE\n";
    for (int i = 0; i < r; ++i) {
      cout << f[i] << endl;
    }
  }
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
