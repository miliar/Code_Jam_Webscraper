#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;
typedef int64_t i64;

i64 R, C;
char B[55][55];

int UP = 0;
int DOWN = 1;
int LEFT = 2;
int RIGHT = 3;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int newdir1[4] = {RIGHT, LEFT, DOWN, UP};
int newdir2[4] = {LEFT, RIGHT, UP, DOWN};

bool explore(int r, int c, int dir, bool write, vector<vector<vector<pair<i64, bool>>>>& covered, pair<i64, bool> shooter) {
  if (r < 0 || r >= R || c < 0 || c >= C)
    return true;
  if (B[r][c] == '|' || B[r][c] == '-')
    return false;
  if (B[r][c] == '#')
    return true;
  if (B[r][c] == '.') {
    if (write) {
      covered[r][c].push_back(shooter);
    }
    return explore(r+dr[dir], c + dc[dir], dir, write, covered, shooter);
  }
  if (B[r][c] == '/') {
    i64 nd = newdir1[dir];
    return explore(r + dr[nd], c + dc[nd], nd, write, covered, shooter);
  }
  if (B[r][c] == '\\') {
    i64 nd = newdir2[dir];
    return explore(r + dr[nd], c + dc[nd], nd, write, covered, shooter);
  }
  assert(false);
}

bool visited[110][2];
vector<pair<i64, bool>> G[110][2];
bool con_recur(pair<i64, bool> at, pair<i64, bool> end) {
  if (at == end) {
    return true;
  }
  if (visited[at.first][at.second]) {
    return false;
  }
  visited[at.first][at.second] = true;
  for (auto e : G[at.first][at.second]) {
    if (con_recur(e, end)) {
      return true;
    }
  }
  return false;
}
bool connected(pair<i64, bool> start, pair<i64, bool> end) {
  memset(visited, 0, sizeof(visited));
  return con_recur(start, end);
}

void recur(pair<i64, bool> at, vector<i64>& set) {
  if (set[at.first] != -1) {
    return;
  }
  set[at.first] = at.second ? 1 : 0;
  for (auto e : G[at.first][at.second]) {
    recur(e, set);
  }
}

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    scanf("%lld %lld", &R, &C);
    for (i64 i = 0; i < R; i++) {
      char buf[1000];
      scanf("%s", buf);
      for (i64 j = 0; j < C; j++)
        B[i][j] = buf[j];
    }

    // For each cell, list of covered by index, position
    vector<vector<vector<pair<i64, bool>>>> covered(R, vector<vector<pair<i64, bool>>>(C));
    vector<pair<i64, i64>> shooter;
    vector<bool> shooter_can_up;
    vector<bool> shooter_can_left;

    for (i64 r = 0; r < R; r++) {
      for (i64 c = 0; c < C; c++) {
        if (B[r][c] == '|' || B[r][c] == '-') {
          auto shooter_up = make_pair<i64, bool>(shooter.size(), true);
          if (explore(r-1, c, UP, false, covered, shooter_up) && explore(r+1, c, DOWN, false, covered, shooter_up)) {
            explore(r-1, c, UP, true, covered, shooter_up); 
            explore(r+1, c, DOWN, true, covered, shooter_up);
            shooter_can_up.push_back(true);
          } else {
            shooter_can_up.push_back(false);
          }
          auto shooter_right = make_pair<i64, bool>(shooter.size(), false);
          if (explore(r, c-1, LEFT, false, covered, shooter_right) && explore(r, c+1, RIGHT, false, covered, shooter_right)) {
            explore(r, c-1, LEFT, true, covered, shooter_right); 
            explore(r, c+1, RIGHT, true, covered, shooter_right);
            shooter_can_left.push_back(true);
          } else {
            shooter_can_left.push_back(false);
          }
          shooter.push_back(make_pair(r, c));
        }
      }
    }

    for (i64 i = 0; i < 110; i++) {
      for (i64 j = 0; j < 2; j++) {
        G[i][j].clear();
      }
    }
    bool ok = true;
    for (i64 r = 0; r < R; r++) {
      for (i64 c = 0; c < C; c++) {
        if (B[r][c] != '.')
          continue;
        auto l = covered[r][c];
        assert(l.size() <= 2);
        if (l.size() == 0) {
          ok = false;
        } else if (l.size() == 1) {
          G[l[0].first][!l[0].second].push_back(l[0]);
        } else {
          G[l[0].first][!l[0].second].push_back(l[1]);
          G[l[1].first][!l[1].second].push_back(l[0]);
        }
      }
    }

    i64 num_set = 0;
    vector<i64> set(shooter.size(), -1);
    for (i64 i = 0; i < shooter.size(); i++) {
      if (set[i] != -1) {
        continue;
      }
      bool timpf = !shooter_can_up[i] || connected(make_pair(i, true), make_pair(i, false));
      bool fimpt = !shooter_can_left[i] || connected(make_pair(i, false), make_pair(i, true));
      if (timpf && fimpt) {
        ok = false;
        break;
      } else if (timpf) {
        recur(make_pair(i, false), set);
      } else if (fimpt) {
        recur(make_pair(i, true), set);
      }
    }
    if (!ok) {
      printf("Case #%lld: IMPOSSIBLE\n", zz);
      continue;
    }
      printf("Case #%lld: POSSIBLE\n", zz);
    for (i64 i = 0; i < shooter.size(); i++) {
      if (set[i] != -1) {
        continue;
      }
      recur(make_pair(i, false), set);
    }
    for (i64 i = 0; i < shooter.size(); i++) {
      B[shooter[i].first][shooter[i].second] = set[i] == 1 ? '|' : '-';
    }
    for (i64 r = 0; r < R; r++) {
      for (i64 c = 0; c < C; c++) {
        printf("%c", B[r][c]);
      }
      printf("\n");
    }
  }
}
