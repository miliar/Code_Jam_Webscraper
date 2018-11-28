#include <iostream>
#include <queue>

#include <algorithm>
#include <vector>
#include <map>
#include <iomanip>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int C, R, M;
vector<string> mm;

vector<vector<int> > turret;
vector<pair<int, int>> turrets;
vector<pair<int, int>> soldiers;
vector<vector<int> > edge;
vector<vector<int> > fffs;

void init() {
    turret.assign(R, vector<int>(C, -1));
    turrets.clear();
    int t = 0;
    for (int y = 0; y < R; ++y) for (int x = 0; x < C; ++x) if (mm[y][x] == 'T') {
                turrets.emplace_back(y, x);
                turret[y][x] = t;
                ++t;
            }

    edge.clear();
    fffs.clear();
}

vector<int> vis(int y, int x) {
    vector<int> r;
    vector<int> ff(C * R, -1);
    ff[y*C+x] = M;
    queue<pair<int, int> > Q;
    Q.push(make_pair(y, x));
    while (Q.size()) {
        int cy = Q.front().first, cx = Q.front().second;
        Q.pop();
        if (!ff[cy*C+cx]) break;
#define TRY(dx, dy) ({                                                  \
                int nx = cx + dx;                                       \
                int ny = cy + dy;                                       \
                if (nx >= 0 && nx < C && ny >= 0 && ny < R && mm[ny][nx] != '#' && ff[ny*C+nx] == -1) { \
                    ff[ny*C+nx] = ff[cy*C+cx] - 1;                      \
                    Q.push(make_pair(ny, nx));                          \
                }                                                       \
            })
        TRY(-1, 0);
        TRY(1, 0);
        TRY(0, -1);
        TRY(0, 1);
#undef TRY
    }
    for (int i = 0; i < turrets.size(); ++i) {
        int cy = turrets[i].first, cx = turrets[i].second;
#define TRY(dx, dy) ({                                                  \
                int nx = cx;                                            \
                int ny = cy;                                            \
                bool visible = false;                                   \
                while (1) {                                             \
                    if (ff[ny*C+nx] >= 0) {                             \
                        visible = true;                                 \
                        break;                                          \
                    }                                                   \
                    nx += dx;                                           \
                    ny += dy;                                           \
                    if (!(nx >= 0 && nx < C && ny >= 0 && ny < R && mm[ny][nx] != '#')) break; \
                }                                                       \
                visible;                                                \
            })
        if (TRY(-1, 0) || TRY(1, 0) || TRY(0, -1) || TRY(0, 1)) {
            r.push_back(i);
        }
#undef TRY
    }
fffs.push_back(move(ff));
    return r;
}

void edges() {
    int s = 0;
    edge.clear();
    fffs.clear();
    soldiers.clear();
    for (int y = 0; y < R; ++y) for (int x = 0; x < C; ++x) if (mm[y][x] == 'S') {
          soldiers.push_back(make_pair(y, x));
                edge.push_back(vis(y, x));
                ++s;
            }
}

vector<int> assn;
vector<int> back;
vector<bool> visited;

bool dfs(int i) {
  if (visited[i]) return false;
  visited[i] = true;
  for (int j : edge[i]) {
    if (back[j] == -1 || dfs(back[j])) {
      assn[i] = j;
      back[j] = i;
      return true;
    }
  }
  return false;
}

int bip() {
    assn.assign(edge.size(), -1);
    back.assign(turrets.size(), -1);
    int r = 0;
    for (int i = 0; i < edge.size(); ++i) {
      visited.assign(edge.size(), false);
        if (dfs(i)) ++r;
    }
    return r;
}

vector<bool> s_shot;
vector<bool> t_shot;

void execute(int i);
void execute() {
  s_shot.assign(edge.size(), false);
  t_shot.assign(turrets.size(), false);
  for (int i = 0; i < edge.size(); ++i) {
    execute(i);
  }
}

void execute(int i) {
    if (s_shot[i] || assn[i] < 0) return;
    s_shot[i] = true;
    int t = assn[i];
    const auto& ff = fffs[i];
        int cy = turrets[t].first, cx = turrets[t].second;
        int vy, vx;
#define TRY(dx, dy) ({                                                  \
                int nx = cx;                                            \
                int ny = cy;                                            \
                bool visible = false;                                   \
                while (1) {                                             \
                    if (ff[ny*C+nx] >= 0) {                             \
                        visible = true;                                 \
                        vy = ny; \
                        vx = nx; \
                        break;                                          \
                    }                                                   \
                    nx += dx;                                           \
                    ny += dy;                                           \
                    if (!(nx >= 0 && nx < C && ny >= 0 && ny < R && mm[ny][nx] != '#')) break; \
                }                                                       \
                visible;                                                \
            })
        if (TRY(-1, 0) || TRY(1, 0) || TRY(0, -1) || TRY(0, 1)) {
        } else {
          assert(!"Oh no");
        }
#undef TRY
        vector<pair<int, int> > p;
        while (1) {
          p.push_back(make_pair(vy, vx));
          if (vy == soldiers[i].first && vx == soldiers[i].second) break;
          int nnx = -1, nny = -1;
#define TRY(dx, dy) ({                                                  \
              int nx = vx + dx;                                         \
              int ny = vy + dy;                                         \
              if (nx >= 0 && nx < C && ny >= 0 && ny < R && mm[ny][nx] != '#' && ff[ny*C+nx] == ff[vy*C+vx]+1) { \
                nnx = nx;                                               \
                nny = ny;                                               \
              }                                                         \
            })
          TRY(-1, 0);
          TRY(1, 0);
          TRY(0, -1);
          TRY(0, 1);
assert(nnx >= 0);
#undef TRY
vy = nny;
vx = nnx;
        }
        reverse(p.begin(), p.end());
        for (auto&& pos : p) {
          int cy = pos.first, cx = pos.second;
#define TRY(dx, dy) ({                                                  \
              int nx = cx;                                              \
              int ny = cy;                                              \
              while (1) {                                               \
                if (turret[ny][nx] >= 0 && !t_shot[turret[ny][nx]]) {   \
                  if (back[turret[ny][nx]] >= 0) {                      \
                    execute(back[turret[ny][nx]]);                      \
                  }                                                     \
                  if (!t_shot[turret[ny][nx]]) {                        \
                    back[assn[i]] = -1;                                 \
                    assn[i] = turret[ny][nx];                           \
                    back[turret[ny][nx]] = i;                           \
                    printf("%d %d\n", i+1, turret[ny][nx]+1);           \
                    s_shot[i] = true;                                   \
                    t_shot[turret[ny][nx]] = true;                      \
                    return;                                             \
                  }                                                     \
                }                                                       \
                  nx += dx;                                             \
                  ny += dy;                                             \
                  if (!(nx >= 0 && nx < C && ny >= 0 && ny < R && mm[ny][nx] != '#')) break; \
                }                                                       \
            })

          TRY(-1, 0);
          TRY(1, 0);
          TRY(0, -1);
          TRY(0, 1);
#undef TRY
        }
printf("%d %d\n", i, assn[i]+1);
s_shot[i] = true;
t_shot[assn[i]] = true;
}

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        cin >> C >> R >> M;
        mm.resize(R);
        for (int i = 0; i < R; ++i) cin >> mm[i];

        init();

        // Which turrets can we shoot?
        edges();

        // Phase 1: pick your turret
        int r = bip();
        printf("Case #%d: %d\n", caseno, r);

        // Phase 2: shoot the turrets
        execute();
    }
}
