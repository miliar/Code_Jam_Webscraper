#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

const int maxn = 1000;

int n, m;
char map0[maxn][maxn];
char map1[maxn][maxn];
bool mapx[maxn][maxn];
bool mapj[maxn][maxn];
bool have1[maxn];
bool have2[maxn];
bool valid[maxn];

// maxflow::clear(int n);
// maxflow::addedge(int u, int v, int cap);
// maxflow::solve(int s, int t);

namespace maxflow {
  const int maxn = 1000, maxm = 1000000;
  const int inf = 0x7fffffff;
  
  int n, m, s, t;
  vector<int> g[maxn];
  
  struct edge {
    int v, cap;
  } ge[maxm * 2];

  void clear(int n1) {
    n = n1; m = 0;
    for (int i = 0; i < n; ++i) {
      g[i].clear();
    }
  }

  inline void addedge(int u, int v, int cap) {
    g[u].push_back(m);
    ge[m++] = (edge){v, cap};
    g[v].push_back(m);
    ge[m++] = (edge){u, 0};
  }

  int it[maxn], gap[maxn], h[maxn];

  int isap(int u, int flow) {
    if (u == t) {
      return flow;
    }
    int sum = 0;
    for (int &i = it[u]; i < (int)g[u].size(); ++i) {
      edge &e = ge[g[u][i]], &rev = ge[g[u][i] ^ 1];
      if (e.cap && h[u] == h[e.v] + 1) {
        int now = isap(e.v, min(flow - sum, e.cap));
        e.cap -= now; rev.cap += now;
        if ((sum += now) == flow) {
          return flow;
        }
      }
    }
    it[u] = 0;
    if (!--gap[h[u]]) {
      h[s] = n;
    }
    ++gap[++h[u]];
    return sum;
  }

  int solve(int s1, int t1) {
    s = s1; t = t1;
    memset(it, 0, sizeof it);
    memset(gap, 0, sizeof gap);
    memset(h, 0, sizeof h);
    gap[0] = n;
    int flow = 0;
    while (h[s] < n) {
      flow += isap(s, inf);
    }
    return flow;
  }
}

int main(void) {
  int t;
  scanf("%d", &t);
  for (int id = 1; id <= t; ++id) {
    scanf("%d%d", &n, &m);
    memset(map0, ' ', sizeof map0);
    for (int i = 0; i < m; ++i) {
      char type[2];
      int x, y;
      scanf("%s%d%d", type, &x, &y);
      map0[x - 1][y - 1] = type[0];
    }
    memset(have1, 0, sizeof have1);
    memset(have2, 0, sizeof have2);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        mapx[i][j] = map0[i][j] == 'o' || map0[i][j] == 'x';
        mapj[i][j] = map0[i][j] == 'o' || map0[i][j] == '+';
        if (mapx[i][j]) {
          have1[i] = true;
          have2[j] = true;
        }
      }
    }
    for (int i = 0; i < n; ++i) {
      if (!have1[i]) {
        for (int j = 0; j < n; ++j) {
          if (!have2[j]) {
            mapx[i][j] = true;
            have1[i] = true;
            have2[j] = true;
            break;
          }
        }
      }
    }
    maxflow::clear(n * 4);
    memset(valid, 1, sizeof valid);
    int ans = n;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        int id1 = i + j;
        int id2 = i - j + n - 1 + n + n - 1;
        if (mapj[i][j]) {
          valid[id1] = false;
          valid[id2] = false;
          ++ans;
        } else {
          maxflow::addedge(id1, id2, 1);
        }
      }
    }
    for (int i = 0; i < n + n - 1; ++i) {
      if (valid[i]) {
        maxflow::addedge(4 * n - 2, i, 1);
      }
      if (valid[i + n + n - 1]) {
        maxflow::addedge(i + n + n - 1, 4 * n - 1, 1);
      }
    }
    ans += maxflow::solve(4 * n - 2, 4 * n - 1);

    for (int i = 0; i < n + n - 1; ++i) {
      for (int j = 0; j < (int)maxflow::g[i].size(); ++j) {
        maxflow::edge &e = maxflow::ge[maxflow::g[i][j]];
        if (e.v >= n + n - 1 && e.v < 4 * n - 2 && e.cap == 0) {
          int x = (i + e.v - 3 * n + 2) / 2;
          int y = i - x;
          mapj[x][y] = true;
        }
      }
    }

    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        map1[i][j] = (mapx[i][j] && mapj[i][j]) ? 'o' : mapx[i][j] ? 'x' :
          mapj[i][j] ? '+' : ' ';
        if (map1[i][j] != map0[i][j]) {
          ++cnt;
        }
      }
    }
    printf("Case #%d: %d %d\n", id, ans, cnt);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        map1[i][j] = (mapx[i][j] && mapj[i][j]) ? 'o' : mapx[i][j] ? 'x' :
          mapj[i][j] ? '+' : ' ';
        if (map1[i][j] != map0[i][j]) {
          printf("%c %d %d\n", map1[i][j], i + 1, j + 1);
        }
      }
    }
  }
  return 0;
}
