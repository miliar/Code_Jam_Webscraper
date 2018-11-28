/* Written by Filip Hlasek 2017 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

#define FOR(i, a, b)   for (int i = (a); i <= (b); i++)
#define FORD(i, a, b)  for (int i = (a); i >= (b); i--)
#define REP(i, b)      for (int i =  0 ; i <  (b); i++)

using namespace std;

#define MAXN 55
int N, M;
char m[MAXN][MAXN];

int shooter_ans[MAXN * MAXN], shooter_x[MAXN * MAXN], shooter_y[MAXN * MAXN];
bool shooter_possible[MAXN * MAXN][2];
vector<int> shooter_id[MAXN][MAXN];
vector<bool> shooter_direction[MAXN][MAXN];
vector< pair<int, int> > shooter_cells[2][MAXN * MAXN];

bool isWall(int x, int y) {
  if (x < 0 || y < 0 || x >= N || y >= M) return true;
  return m[x][y] == '#';
}

bool isShooter(int x, int y) {
  return m[x][y] == '-' || m[x][y] == '|';
}

/**
 * Direction:
 *   0 - Down
 *   1 - Right
 *   2 - Up
 *   3 - Left
 */

bool shoot(int x, int y, int d, int id, int direction, bool add = false) {
  while (true) {
    if (isWall(x, y)) return true;
    if (isShooter(x, y)) return false;
    if (m[x][y] == '.' || m[x][y] == '\\' || m[x][y] == '/') {
      if (add) {
        shooter_cells[direction][id].push_back(make_pair(x, y));
        shooter_id[x][y].push_back(id);
        shooter_direction[x][y].push_back(direction);
      }
      if (d == 0) x++;
      if (d == 1) y++;
      if (d == 2) x--;
      if (d == 3) y--;
    }
  }
}

bool placeShooter(int x, int y, int id) {
  shooter_ans[id] = -1;
  shooter_cells[0][id].clear();
  shooter_cells[1][id].clear();
  shooter_possible[id][0] = shooter_possible[id][1] = false;
  shooter_x[id] = x;
  shooter_y[id] = y;
  if (shoot(x + 1, y, 0, id, 0) && shoot(x - 1, y, 2, id, 0)) {
    shoot(x + 1, y, 0, id, 0, true);
    shoot(x - 1, y, 2, id, 0, true);
    shooter_possible[id][0] = true;
  }
  if (shoot(x, y + 1, 1, id, 1) && shoot(x, y - 1, 3, id, 1)) {
    shoot(x, y + 1, 1, id, 1, true);
    shoot(x, y - 1, 3, id, 1, true);
    shooter_possible[id][1] = true;
  }
  if (!shooter_possible[id][0]) shooter_ans[id] = 1;
  if (!shooter_possible[id][1]) shooter_ans[id] = 0;
  return shooter_possible[id][0] || shooter_possible[id][1];
}

bool isDone(int x, int y) {
  if (m[x][y] != '.') return true;
  REP(i, shooter_id[x][y].size()) {
    if (shooter_ans[shooter_id[x][y][i]] == shooter_direction[x][y][i]) {
      return true;
    }
  }
  return false;
}

void solve() {
  scanf("%d%d", &N, &M);
  REP(i, N) scanf("%s", m[i]);
  int shooter = 0;
  REP(i, N) REP(j, M) {
    shooter_id[i][j].clear();
    shooter_direction[i][j].clear();
  }
  REP(i, N) REP(j, M) if (isShooter(i, j)) {
    if (!placeShooter(i, j, shooter++)) {
      // printf("Cannot place %d %d\n", i, j);
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  bool change = true;
  int iteration = 0;
  while (change) {
    iteration++;
    // printf("iteration: %d\n", iteration);
    while (change) {
      change = false;
      REP(x, N) REP(y, M) if (m[x][y] == '.') {
        if (isDone(x, y)) continue;
        int options = 0;
        REP(i, shooter_id[x][y].size()) {
          int id = shooter_id[x][y][i];
          if (shooter_ans[id] == -1 && shooter_possible[id][shooter_direction[x][y][i]]) {
            options++;
          }
        }
        if (options == 0) {
          // printf("Cell %d %d has 0 options\n", x, y);
          printf("IMPOSSIBLE\n");
          return;
        }
        if (options == 1) {
          REP(i, shooter_id[x][y].size()) {
            int id = shooter_id[x][y][i];
            if (shooter_ans[id] == -1 && shooter_possible[id][shooter_direction[x][y][i]]) {
              shooter_ans[id] = shooter_direction[x][y][i];
              change = true;
            }
          }
        }
      }
      REP(id, shooter) if (shooter_ans[id] == -1) {
        bool r[2];
        r[0] = r[1] = false;
        REP(x, N) REP(y, M) {
          if (isDone(x, y)) continue;
          REP(i, shooter_id[x][y].size()) if (id == shooter_id[x][y][i]) {
            r[shooter_direction[x][y][i]] = true;
          }
        }
        if (!r[0]) { shooter_ans[id] = 1; change = true; }
        if (!r[1]) { shooter_ans[id] = 0; change = true; }
      }
    }
    change = false;
    REP(i, shooter) if (shooter_ans[i] == -1) {
      change = true;
      shooter_ans[i] = 0;
    }
  }
  printf("POSSIBLE\n");
  REP(i, shooter) m[shooter_x[i]][shooter_y[i]] = (shooter_ans[i] ? '-' : '|');
  REP(i, N) printf("%s\n", m[i]);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
