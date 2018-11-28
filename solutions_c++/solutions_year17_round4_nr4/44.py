#define NDEBUG
#include <cstdint>
#include <cstring>
#include <functional>
#include <iostream>
#include <queue>
#include <tuple>
#include <utility>
using namespace std;

#define MINUSONE(v) memset((v), -1, sizeof (v))
#define ZERO(v) memset((v), 0, sizeof (v))
template <typename T> inline int get_bit(const T &x, int index) {
  return int((x >> index) & 1);
}
template <typename T> inline T kill_bit(const T &x, int index) {
  return x & ~((T)1 << index);
}
template<typename T, typename U> inline bool makemax(T &res, const U &x) {
  if (x > res) {
    res = x;
    return true;
  }
  return false;
}

const int MAX = 30;
const int MAXN = 10;
const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

int R, C, M;
char grid[MAX][MAX+1];
int NT, NS;
int ty[MAXN], tx[MAXN], sy[MAXN], sx[MAXN];

bool valid(int y, int x) {
  return y >= 0 && y < R && x >= 0 && x < C && grid[y][x] != '#';
}

int8_t bfs_memo[MAXN][MAXN][1<<10];
bool can(const int s, const int t, const int tmask) {
  auto& ref = bfs_memo[s][t][tmask];
  if (ref != -1) {
    return ref;
  }

  static int16_t dist[MAX][MAX];
  static bool attacked[MAX][MAX];
  static bool goal[MAX][MAX];
  const int16_t INF = 0x3f3f;
  MINUSONE(dist);
  ZERO(attacked);
  ZERO(goal);
  for (int y = 0; y < R; ++y) {
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] == '#') {
        dist[y][x] = INF;
      }
    }
  }

  for (int i = 0; i < MAXN; ++i) {
    if (get_bit(tmask, i)) {
      for (int dir = 0; dir < 4; ++dir) {
        int ny = ty[i], nx = tx[i];
        while (1) {
          ny += dy[dir];
          nx += dx[dir];
          if (!valid(ny, nx) || grid[ny][nx] == '#') {
            break;
          }
          if (i == t) {
            goal[ny][nx] = 1;
          } else {
            attacked[ny][nx] = 1;
          }
        }
      }
    }
  }

  queue<pair<int, int> > q;
  dist[sy[s]][sx[s]] = 0;
  q.push(make_pair(sy[s], sx[s]));
  while (!q.empty()) {
    int y, x;
    tie(y, x) = q.front(); q.pop();
    // dbg(y, x);
    if (goal[y][x]) {
      return (ref = true);
    }
    if (!attacked[y][x] && dist[y][x] < M) {
      for (int dir = 0; dir < 4; ++dir) {
        int ny = y + dy[dir], nx = x + dx[dir];
        if (valid(ny, nx) && grid[ny][nx] != '#' && dist[ny][nx] == -1) {
          dist[ny][nx] = dist[y][x] + 1;
          q.push(make_pair(ny, nx));
        }
      }
    }
  }
  return (ref = false);
}

int8_t memo[1<<MAXN][1<<MAXN];
pair<int8_t, int8_t> move[1<<MAXN][1<<MAXN];
int calc(int smask, int tmask) {
  auto& ref = memo[smask][tmask];
  if (ref != -1) {
    return ref;
  }

  ref = 0;
  ::move[smask][tmask] = make_pair(-1, -1);
  for (int s = 0; s < NS; ++s) {
    if (get_bit(smask, s)) {
      for (int t = 0; t < NT; ++t) {
        if (get_bit(tmask, t) && can(s, t, tmask)) {
          if (makemax(ref, 1 + calc(kill_bit(smask, s), kill_bit(tmask, t)))) {
            ::move[smask][tmask] = make_pair(s, t);
          }
        }
      }
    }
  }
  return ref;
}

void solve() {
  MINUSONE(memo);
  MINUSONE(bfs_memo);
  cin >> C >> R >> M;
  NS = NT = 0;
  for (int y = 0; y < R; ++y) {
    cin >> grid[y];
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] == 'S') {
        sy[NS] = y;
        sx[NS] = x;
        ++NS;
      } else if (grid[y][x] == 'T') {
        ty[NT] = y;
        tx[NT] = x;
        ++NT;
      }
    }
  }

  // dbg(can(0, 0, 3));
  // return;
  pair<int, int> state((1 << NS) - 1, (1 << NT) - 1);
  calc(state.first, state.second);
  cout << int(memo[state.first][state.second]) << '\n';
  while (1) {
    auto m = ::move[state.first][state.second];
    if (m.first == -1) {
      break;
    }
    cout << int(m.first) + 1 << ' ' << int(m.second) + 1 << '\n';
    state.first = kill_bit(state.first, m.first);
    state.second = kill_bit(state.second, m.second);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": ";
    solve();
    cout << flush;
  }
}
